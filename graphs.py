
#We implement the data structures of a graph
class node(object):
    def __init__(self,name):
        """ Assume name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
