#121910313016
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def printTree(self):
        print(self.val)

root = Node(17)
root.printTree()
