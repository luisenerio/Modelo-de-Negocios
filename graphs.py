
#We implement the data structures of a graph
from multiprocessing.sharedctypes import Value


class node(object):
    def __init__(self,name):
        """ Assume name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class edge(object):
    def __init__(self,src,dest):
        """ Src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        pass
    def getDestination(self):
        pass
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    def __init__(self):
        """ edges is a dict mapping each node to a list of its children"""
        self.edges = {}
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate node')
    
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self,name):
        for n in self.edges:
            if n.getName == name:
                return n
        raise ValueError('name')

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'+  dest.getName() + '\n'
        return result[:-1] #omitir salto de linea final

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(node(name))
    g.addEdge(edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
    
print(buildCityGraph(Graph))
