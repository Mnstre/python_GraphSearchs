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
        edgeName = []
        for vertex in self.gdict:
            for conection in self.gdict[vertex]:
                if {conection, vertex} not in edgeName:
                    edgeName.append({vertex, conection})
        return edgeName

    def addVertex(self):
        vertex = input("Vértice a agregar: ")
        if vertex not in self.gdict:
            self.gdict[vertex] = []

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
    value = input("Ingrese una opción:\n0)Mostrar Gráfo\n1)Mostrar Vertices\n2)Mostrar Aristas\n3)Agregar Vertice\n4)Agregar Arista\n")
    g.switch(value)
#############################################