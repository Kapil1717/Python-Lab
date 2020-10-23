#121910313016

class Node:
    def __init__(self, data):
        self.data = data;
        self.previous = None;
        self.next = None;

class LinkedList:
   def __init__(self):
        self.head = None
        self.tail = None

   def addAtStart(self, data):        
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


List1 = LinkedList()
List1.addAtStart(17)
List1.display()
List1.addAtStart(18)
List1.display()
List1.addAtStart(45)
List1.display()

