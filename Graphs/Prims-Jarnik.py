import heapq


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.pred = None
        self.neighbors = []

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsJarnik(object):
    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.priorityEdges = []
        self.total = 0

    def computeMST(self, vertex):
        self.unvisitedList.remove(vertex)

        while self.unvisitedList:
            for edge in vertex.neighbors:
                if edge.target in self.unvisitedList:
                    heapq.heappush(self.priorityEdges, edge)

            min_edge = heapq.heappop(self.priorityEdges)
            self.spanningTree.append(min_edge)
            print("{} - {}".format(min_edge.start, min_edge.target))
            self.total += min_edge.weight

            vertex = min_edge.target
            self.unvisitedList.remove(vertex)

    def getMST(self):
        return self.spanningTree


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(100, node1, node2)
edge2 = Edge(100, node2, node1)
edge3 = Edge(1000, node1, node3)
edge4 = Edge(1000, node3, node1)
edge5 = Edge(0.01, node3, node2)
edge6 = Edge(0.01, node2, node3)

node1.neighbors.append(edge1)
node1.neighbors.append(edge3)
node2.neighbors.append(edge2)
node2.neighbors.append(edge6)
node3.neighbors.append(edge4)
node3.neighbors.append(edge5)

unvisitedList = []
unvisitedList.append(node1)
unvisitedList.append(node2)
unvisitedList.append(node3)

algorithm = PrimsJarnik(unvisitedList)
algorithm.computeMST(node2)
