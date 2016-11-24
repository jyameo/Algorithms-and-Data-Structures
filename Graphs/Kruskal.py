class Node(object):
    def __init__(self, height, id, parent):
        self.height = height
        self.id = id
        self.parent = parent


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None


class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet(object):

    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.roots = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)

    def find(self, node):
        # find root
        current = node
        while current.parent:
            current = current.parent

        root = current

        # path compression
        current = node
        while current is not root:
            tmp = current.parent
            current.parent = root
            current = tmp

        return root.id

    def merge(self, node1, node2):
        id1 = self.find(node1)
        id2 = self.find(node2)

        if id1 == id2:
            # same set
            return

        root1 = self.roots[id1]
        root2 = self.roots[id2]

        if root1.height < root2.height:
            root1.parent = root2
        elif root1.height > root2.height:
            root2.parent = root1
        else:
            root1.parent = root2
            root2.height += 1

    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.roots), None)
        vertex.node = node
        self.roots.append(node)
        self.setCount += 1
        self.nodeCount += 1


class KruskalAlgorithm(object):
    def spanningTree(self, vertexList, edgeList):
        disjointSet = DisjointSet(vertexList)
        spanningTree = []
        edgeList.sort()
        for edge in edgeList:
            u = edge.start
            v = edge.target
            if disjointSet.find(u.node) is not disjointSet.find(v.node):
                spanningTree.append(edge)
                disjointSet.merge(u.node, v.node)

        for edge in spanningTree:
            print("{} - {}".format(edge.start.name, edge.target.name))


vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)
vertexList.append(vertex7)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)

algorithm = KruskalAlgorithm()
algorithm.spanningTree(vertexList, edgeList)
