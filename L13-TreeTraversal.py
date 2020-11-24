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


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self,root):
        if root:
            print(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
        return

    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)
        return

    def post_order(self,root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.val)
        return

B=BinaryTree()
a = int(input("Enter the Root:"))
B.root=Node(a)
n = int(input("How many elements you want to add: "))
print("Enter "+ str(n) + " elements you want to add:")
for i in range(n):
    B.root.insert(int(input()))
print("Pre order Traversal")
print(B.pre_order(B.root))
print("In order Traversal")
print(B.in_order(B.root))
print("Post order Traversal")
print(B.post_order(B.root))
    

