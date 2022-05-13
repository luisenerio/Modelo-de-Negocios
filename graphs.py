
#We implement the data structures of a graph
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

