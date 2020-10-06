#121910313016
#define a class
class Node:
    def __init__(self, data):
        self.data = data;
        self.previous = None;
        self.next = None;

class InsertStart:
   def __init__(self):
        self.head = None
        self.tail = None

   def addAtStart(self, data):
        # Create a new node
        newNode = Node(data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.head.previous = newNode
            newNode.next = self.head
            newNode.previous = None
            self.head = newNode
   def display(self):

        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Adding a node to the start of the list: ")
        while (current != None):
            print(current.data)
            current = current.next
        print()


dList = InsertStart()
dList.addAtStart(1)
dList.display()
dList.addAtStart(2)
dList.display()
dList.addAtStart(3)
dList.display()
dList.addAtStart(4)
dList.display()
dList.addAtStart(5)
dList.display()
