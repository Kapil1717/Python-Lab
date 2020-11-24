#121910313016
class Node:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val) 
        else:
            self.val = val

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

root = Node(17)
root.insert(45)
root.insert(18)
root.insert(77)
root.insert(7)
root.insert(10)
root.insert(18)
root.insert(19)
root.insert(99)
root.insert(35)
root.insert(67)
root.insert(89)
root.insert(999)
root.printTree()
