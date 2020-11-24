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
            elif val > self.val:
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
n = int(input("How many elements you want to add: "))
print("Enter "+ str(n) + " elements you want to add:")
for i in range(n):
    root.insert(int(input()))
print("Nodes in the binary tree are:")
root.printTree()
