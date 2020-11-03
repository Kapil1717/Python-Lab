class Stacks:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

def postfix(exp):
    exp = exp.split()
    stack=Stacks()
    for i in exp:
        if i.isdigit():
            stack.push(int(i))
        elif i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a)+int(b))
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b)-int(a))
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a)*int(b))
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b)/int(a))
    return stack.pop()

exp = input("Enter the expression : ")
val = postfix(exp)
print("Required value is : ")
print(val)
