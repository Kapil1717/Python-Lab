 #121910313016

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


l = LinkedList()
l.head = Node(17)
second = Node(18)
third  = Node(19)
fourth = Node(20)
l.head.next = second
second.next = third
third.next = fourth
l.print_list()
