class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    #  best case:O(log(n)) -> (balanced) | worst case: O(n) -> (sorted list)
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            cur = self.root
            while cur:
                if data < cur.data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break

    # O (log n)
    def getMin(self):
        cur = self.root
        if cur.left:
            cur = cur.left
        return cur.data

    # O (log n)
    def getMax(self):
        cur = self.root
        if cur.right:
            cur = cur.right

    def printTree(self):
        if self.root:
            self.inOrderTraversal(self.root)
        else:
            print('The tree is Empty')

    # O (n)
    def inOrderTraversal(self, root):
        if root:
            if root.left:
                self.inOrderTraversal(root.left)
            print(root.data)
            if root.right:
                self.inOrderTraversal(root.right)

    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root)

    # O (log n)
    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        # Found node to remove!
        else:
            # case 1: leaf node
            if not node.left and not node.right:
                print("removing leaf node")
                del node
                return None

            # case 2: single child
            if not node.left or not node.right:
                if node.right:
                    print("removing node with single right child")
                    tmp = node.right
                    del node
                    return tmp
                else:
                    print("removing node with single left child")
                    tmp = node.left
                    del node
                    return tmp

            # case 3: both children
            print("removing node with both children")
            pred = self.getPredecessor(node.left)
            node.data = pred.data
            node.left = self.removeNode(pred.data, node.left)
        return node

    # O (log n)
    def getPredecessor(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(32)
    bst.insert(10)
    bst.insert(45)
    bst.insert(98)
    bst.insert(1)
    bst.printTree()

    bst.remove(1)
    bst.printTree()
    bst.remove(98)
    bst.printTree()
    bst.remove(32)
    bst.printTree()
