class Node(object):
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False
        self.predecessor = None


class DepthFirstSearch(object):

    def dfs(self, startNode):
        startNode.visited = True
        print(startNode.data)

        for node in startNode.neighbors:
            if not node.visited:
                self.dfs(node)

    def dfs_iterative(self, startNode):
        stack = [startNode]
        startNode.visited = True

        while stack:
            # LIFO
            current = stack.pop()
            print(current.data)

            for node in current.neighbors:
                if not node.visited:
                    node.visited = True
                    stack.append(node)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')


node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node4)
node4.neighbors.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)
#dfs.dfs_iterative(node1)
