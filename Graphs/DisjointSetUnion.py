# See Kruskal.py for full use of DSU

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
