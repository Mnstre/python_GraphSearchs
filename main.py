#   Graph Searches Program
#   Create, Edit and Eliminate Vertex and Edges of a Graph
#
#   Mnstre @ September, 2021
class graphManager:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    def getVertex(self):
        return list(self.gdict.keys())
    def getEdges(self):
        return list(self.findEdges())
    def findEdges(self):
        return 0

graph = {
    "a" : ["b", "c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

g = graphManager(graph)
print(graph)
print(g.getVertex())
