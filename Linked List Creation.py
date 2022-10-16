class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None 
class LinkedList:
    def __int__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n=self.head
        while n:
            print(n.data)
            n=n.ref
                
node1 =Node(10)
node2=Node(2)
q1=LinkedList()
q1.head=node1
node1.ref=node2
q1.print_ll()
