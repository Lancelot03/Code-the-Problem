class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class NodeOperation:
    def pushNode(self, head_ref, data_val):
        new_node = Node(data_val)
        new_node.next = head_ref
        head_ref = new_node
        return head_ref
    def printNode(self, head):
        while (head != None):
            print('%d->' % head.data, end="")
            head = head.next
        print("NULL")
    def getLen(self, head):
        temp = head
        len = 0
 
        while (temp != None):
            len += 1
            temp = temp.next
 
        return len
 
    def printMiddle(self, head):
        if head != None:
            len = self.getLen(head)
            temp = head
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
            print('The middle element is [%d]' % temp.data)
 
head = None
temp = NodeOperation()
for i in range(5, 0, -1):
    head = temp.pushNode(head, i)
    temp.printNode(head)
    temp.printMiddle(head)
