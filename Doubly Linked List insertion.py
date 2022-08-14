def push(self, new_data):
    new_node = Node(data = new_data)
    new_node.next = self.head
    new_node.prev = None
    if self.head is not None:
        self.head.prev = new_node
    self.head = new_node 
