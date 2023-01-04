class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.__dict__)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return self
        node = self.root
        while True:
            if value > node.value:
                if not node.right:
                    node.right = Node(value)
                    return self
                node = node.right
            elif value < node.value:
                if not node.left:
                    node.left = Node(value)
                    return self
                node = node.left
            else:
                return None


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(13)
    tree.insert(11)
    tree.insert(2)
    tree.insert(10)
    tree.insert(7)
    print(tree.root)
