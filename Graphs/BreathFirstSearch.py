class Node(object):
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False
        self.predecessor = None


class BreathFirstSearch(object):

    def bfs(self, startNode):
        queue = [startNode]
        startNode.visited = True

        while queue:
            # FIFO
            current = queue.pop(0)
            print(current.data)

            for node in current.neighbors:
                if not node.visited:
                    node.visited = True
                    queue.append(node)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')


node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node4)
node4.neighbors.append(node5)

bfs = BreathFirstSearch()
bfs.bfs(node1)
