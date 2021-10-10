#   Graph Searches Program
#   Create, Edit and Eliminate Vertex and Edges of a Graph
#
#   Mnstre @ September, 2021
#############################################
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
        edgeList = []
        vertexList = self.getVertex()
        for vStart in vertexList:
            for vEnd in self.gdict[vStart]:
                if {vStart, vEnd} not in edgeList:
                    edgeList.append({vStart, vEnd})
        return edgeList

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

    def addEdge(self):
        vertex1 = input("Edge start: ")
        vertex2 = input("Edge end: ")
        edge = sorted(vertex1, vertex2)
        #
        #edge = set(edge)
        #(vertex1, vertex2) = tuple(edge)
        #if vertex1 in self.gdict:
        #    self.gdict[vertex1].append(vertex2)
        #else:
        #    self.gdict[vertex1] = [vertex2]
        #
    def switch(self, value):
        switcher = {
            '0': self.getGraph,
            '1': self.getVertex,
            '2': self.getEdges,
            '3': self.addVertex,
            '4': self.addEdge
        }
        func = switcher.get(value, lambda: "Invalid option")
        cadena = func()
        print(cadena)
#############################################
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
    if value == '0':
        print(graph)
    if value == '1':
        print(g.getVertex())
    if value == '2':
        print(g.getEdges())
    if value == '3':
        v = input("Valor del nuevo Vertice:\n")
        g.addVertex(v)
        print(g.getVertex)
    if value == '4':
        e1 = input("Primer enlace:\n")
        e2 = input("Segundo enlace:\n")
        g.addEdge({e1, e2})
        print(g.getEdges())
