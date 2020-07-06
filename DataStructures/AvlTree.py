from BinarySearchTree import BinarySearchTree


class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left, self.right = None, None


class AvlTree(BinarySearchTree):

    def insert(self, data):
        self.root = self.insertNode(self.root, data)

    def insertNode(self, node, data):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insertNode(node.left, data)
        else:
            node.right = self.insertNode(node.right, data)
        node.height = max(self.getHeight(node.left),
                          self.getHeight(node.right)) + 1

        return self.fixViolation(node, data)

    def fixViolation(self, node, data):
        balance = self.getBalance(node)

        # case 1: doubly-left heavy
        if balance > 1 and data < node.left.data:
            print("doubly-left heavy situation")
            return self.rotateRight(node)
        # case 2: doubly-right heavy
        if balance < -1 and data > node.right.data:
            print("doubly-right heavy situation")
            return self.rotateLeft(node)
        # case 3: left-right heavy
        if balance > 1 and data > node.left.data:
            print("left-right heavy situation")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        # case 4: right-left heavy
        if balance < -1 and data < node.right.data:
            print("right-left heavy situation")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node

    def getHeight(self, node):
        if not node:
            return -1
        return node.height

    # > 1 : right rotation
    # < 1 : left rotation
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, node):
        if node:
            print("Right rotation on {}".format(node.data))

            tmp = node.left
            t = tmp.right

            tmp.right = node
            node.left = t

            node.height = max(self.getHeight(node.left),
                              self.getHeight(node.right)) + 1
            tmp.height = max(self.getHeight(tmp.left),
                             self.getHeight(tmp.right)) + 1
            return tmp
        return node

    def rotateLeft(self, node):
        if node:
            print("Left rotation on {}".format(node.data))

            tmp = node.right
            t = tmp.left

            tmp.left = node
            node.right = t

            node.height = max(self.getHeight(node.left),
                              self.getHeight(node.right)) + 1
            tmp.height = max(self.getHeight(tmp.left),
                             self.getHeight(tmp.right)) + 1
            return tmp
        return node

    def printTree(self):
        if self.root:
            self.inOrderTraversal(self.root)
        else:
            print('The tree is Empty')

    def inOrderTraversal(self, root):
        if root:
            if root.left:
                self.inOrderTraversal(root.left)
            print(root.data)
            if root.right:
                self.inOrderTraversal(root.right)

if __name__ == '__main__':
    avl = AvlTree()

    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.insert(6)
    avl.printTree()

    avl.remove(1)
    avl.printTree()

    avl.remove(6)
    avl.printTree()

    avl.remove(4)
    avl.printTree()
