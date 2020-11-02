class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size-=1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            print(data)
        else:
            print(None)
                
    def sizeOfStack(self):
        print(self.size)

    def print(self):
        cur = self.top
        while cur:
            print(cur.data)
            cur = cur.next

st = Stack()
n = int(input("Enter the number of elements you want to push : "))
print("Enter the elements : ")
for i in range(n):
    a = input()
    st.push(a)  
print("Elements in the stack before popping are : ")
st.print()
print("Popped element in the stack is :")
st.pop()
print("Elements in the stack after popping are : ")
st.print()
print("Size of the stack is : ")
st.sizeOfStack()

