class DoubleLinkedList:
    class Node:
        #initialization method
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    #Double linked list initialization
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    '''
    Print the values of a double linked list
    '''
    def print(self):
        arr, cur = [], self.head 
        while cur != None:
            arr.append(cur.data)
            cur = cur.next
        print(arr, self.len)

    #inserts a node at the beggining of the list
    def unshift_node(self, data):
        new_node = self.Node(data)
        if self.len == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.len += 1

    #adds a node to the tail of the list
    def append_node(self, data):
        new_node = self.Node(data)
        if self.len == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.len += 1

    def remove_head(self):
        if self.len == 0:
            return
        self.head = self.head.next
        self.head.prev = None
        self.len -= 1
    
    #deletes the last node from the list
    def pop(self):
        if self.len <= 1:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
    


    
