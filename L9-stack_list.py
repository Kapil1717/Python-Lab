class stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        print(self.items[len(self.items)-1])
        
    def printStack(self):
        print(self.items)

st = stack()
n = int(input("Enter the number of elements you want to push : "))
print("Enter the elements : ")
for i in range(n):
    a = input()
    st.push(a)    
print("Topmost element in the stack is (peek) : ")
st.peek()
print("Stack before popping is : ")
st.printStack()
st.pop()
print("Stack after popping is : " )
st.printStack()    
