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

class BinaryTree:

    def __init__(self):
        self.root = None
    
    def add(self,node):
        sumright = sumleft = 0
        if not self.root:
            print("Tree is empty!")
            sum = 0
        else:
            if node.left:
                sumleft = self.add(node.left)                
            if node.right:
                sumright = self.add(node.right)                
            sum =  node.val + sumright + sumleft
        return sum  


B = BinaryTree()
r = int(input("Enter the root of the tree: "))
B.root = Node(r)
n = int(input("How many elements you want to add: "))
print("Enter "+ str(n) + " elements you want to add:")
for i in range(n):
    B.root.insert(int(input()))
print("Nodes in the binary tree are:")
B.root.printTree()
print("Sum of the values of the nodes is:")
print(B.add(B.root))

