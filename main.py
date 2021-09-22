#   Graph Searches Program
#   Create, Edit and Eliminate Vertex and Edges of a Graph
#
#   Mnstre @ September, 2021
class graphManager:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    def getGraph(self):
        return self.gdict
    def getVertex(self):
        return list(self.gdict.keys())
    def getEdges(self):
        return self.findEdges()

    def findEdges(self):
        edgeName = []
        for vertex in self.gdict:
            for nextVertex in self.gdict[vertex]:
                if {nextVertex, vertex} not in edgeName:
                    edgeName.append({vertex, nextVertex})
        return edgeName
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def switch(self, value):
        switcher = {
            '0': 'getGraph',
            '1': 'getVertex',
            '2': 'getEdges',
            '3': 'addVertex',
            '4': 'addEdge'
        }
        func = switcher.get(value, lambda: "Invalid option")
        
        cadena = self.func()
        print(cadena)

graph = {
    "a" : ["b", "c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

g = graphManager(graph)
while(1):
    value = input("Ingrese una opción:\n1)Mostrar Vertices\n2)Mostrar Aristas\n3)Agregar Vertice\n4)Agregar Arista\n")
    g.switch(value)