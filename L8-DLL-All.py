#121910313016
class Node: 

	def __init__(self, next=None, prev=None, data=None): 
		self.next = next  
		self.prev = prev  
		self.data = data         

class DoublyLinkedList:     

    def __init__(self): 
        self.head = None    

    def append(self, new_data):        
        new_node = Node(data = new_data)   
        new_node.next = self.head 
        new_node.prev = None        
        if self.head is not None: 
            self.head.prev = new_node         
        self.head = new_node  

    def addAtBack(self,new_data):
        new_node = Node(data = new_data)
        last = self.head        
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return 
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last

    def addAfter(self,prev_node,new_data):
        if prev_node is None:
            print("Node doesn't exist!")
            return            
        new_node = Node(data = new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def delete(self,val):
        cur = self.head
        prev_node = None
        found = False
        while not found:
            if cur.data == val:
                found = True
            else:
                prev_node = cur
                cur = prev_node.next
        if prev_node is None:
            cur = cur.next
        else:
            prev_node.next = cur.next

    def length(self):
        cur = self.head
        total_nodes = 0
        while cur is not None:
            total_nodes+=1
            cur = cur.next        
        print(total_nodes)
    
    def search(self,val):
        cur = self.head
        found = False
        while cur is not None and not found:
            if(cur.data == val):
                found = True
            else:
                cur = cur.next
        print(found) 

    def min(self):
        cur = self.head
        if cur == None:
            print("List is empty!")           
        else:
            min = cur.data
            while cur is not None:
                if(min > cur.data):
                    min = cur.data
                cur = cur.next
            print(min)
    
    def max(self):
        cur = self.head
        if cur == None:
            print("List is empty!")           
        else:
            max = cur.data
            while cur is not None:
                if(max < cur.data):
                    max = cur.data
                cur = cur.next
            print(max)

    def printList(self):        
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next     
   

llist = DoublyLinkedList()  
llist.append(45) 
llist.append(18)  
llist.append(17) 
a = int(input('Enter the number you want to add at the begining: '))
llist.append(a)
b = int(input('Enter the number you want to add at the ending:  '))
llist.addAtBack(b)
c = int(input("Enter the number you want to add after the node: "))
llist.addAfter(llist.head.next,c)
d = int(input("Check whether this value is in the Linked List or not: "))
llist.search(d)
print('Number of nodes in the DLL is: ')
llist.length()
print("DLL is: ") 
llist.printList()
e = int(input("Enter the element you want to delete: "))
llist.delete(e)
print("Linked list after the deletion: ")
llist.printList()
print("Minimum key in the Linked list is: ")
llist.min()
print("Maximum key in the Linked list is: ")
llist.max()
  
