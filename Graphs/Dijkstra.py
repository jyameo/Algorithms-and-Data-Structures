from heapq import heappush, heappop
import sys


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.pred = None
        self.neighbors = []
        self.minDistance = sys.maxsize

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, weight, source, target):
        self.weight = weight
        self.source = source
        self.target = target


class Dijkstra():
    def computeShortestPath(self, vertexList, source):
        priorityVertices = []
        source.minDistance = 0
        heappush(priorityVertices, source)

        while priorityVertices:
            current = heappop(priorityVertices)

            for edge in current.neighbors:
                u = edge.source
                v = edge.target
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.pred = u
                    v.minDistance = newDistance
                    heappush(priorityVertices, v)

    def getShortestPath(self, target):
        print('Shortest path to vertex is: ', target.minDistance)

        node = target

        while node:
            print(node)
            node = node.pred


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")
node4 = Vertex("D")
node5 = Vertex("E")
node6 = Vertex("F")
node7 = Vertex("G")
node8 = Vertex("H")

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.neighbors.append(edge1)
node1.neighbors.append(edge2)
node1.neighbors.append(edge3)
node2.neighbors.append(edge4)
node2.neighbors.append(edge5)
node2.neighbors.append(edge6)
node8.neighbors.append(edge7)
node8.neighbors.append(edge8)
node5.neighbors.append(edge9)
node5.neighbors.append(edge10)
node5.neighbors.append(edge11)
node6.neighbors.append(edge12)
node6.neighbors.append(edge13)
node3.neighbors.append(edge14)
node3.neighbors.append(edge15)
node4.neighbors.append(edge16)


vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

algorithm = Dijkstra()
algorithm.computeShortestPath(vertexList, node1)
algorithm.getShortestPath(node7)
