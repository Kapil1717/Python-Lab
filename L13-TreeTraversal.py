#121910313016
class Node:    

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

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
B.root=Node(17)
B.root.left=Node(2)
B.root.right=Node(3)
B.root.left.left=Node(4)
B.root.left.right=Node(5)
B.root.right.left=Node(7)
B.root.right.right=Node(6)
print("Pre order Traversal")
print(B.pre_order(B.root))
print("In order Traversal")
print(B.in_order(B.root))
print("Post order Traversal")
print(B.post_order(B.root))
    

