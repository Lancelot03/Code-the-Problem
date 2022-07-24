class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None 
class LinkedList:
    def __int__(self):
        self.head=None
        
    def begin(self,new_data):    
        q1=Node(new_data)
        q1.ref=self.head
        self.head=q1
        
    def inbet(self,prev,new_data):
        if prev.ref is None:
            print('LL is empty')
            return
        q4 = Node(new_data)
        q4.ref=prev.ref
        prev.ref=q4
        
    def last(self,new_data):
        q2=Node(new_data)
        if self.head==None:
            self.head=q2
            return
        temp=self.head
        while(temp.ref):
            temp=temp.ref
            
        temp.ref=q2
        
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n=self.head
        while n:
            print(n.data)
            n=n.ref
                
h1=Node(2)
h2=Node(3)

k1=LinkedList()
k1.head=h1
h1.ref=h2

k1.begin(1)
k1.inbet(k1.head.ref,5)
k1.last(8)

k1.print_ll()
