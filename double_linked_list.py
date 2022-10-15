class DoubleLinkedList:
    class Node:
        '''
        initialization method
        '''
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    '''
    Double linked list initialization
    '''
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

    '''
    inserts a node at the beggining of the list
    '''
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

    '''
    Adds a node to the tail of the list
    '''
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

    '''
    Removes the head of th elinked list, setting the
    following node as the new head
    '''
    def remove_head(self):
        if self.len == 0:
            return
        self.head = self.head.next
        self.head.prev = None
        self.len -= 1
    
    '''
    Deletes the last node (tail) from the list, setting
    the previous one as the new tail
    '''
    def pop(self):
        if self.len <= 1:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
    
    '''
    Returns a wanted node of the list (Memory allocation)
    '''
    def get_node(self, index):
        if index < 0 or index > self.len-1:
            return
        cur, counter = self.head, 0
        while counter < index:
            cur = cur.next 
            counter += 1
        return cur

    '''
    Returns the value of a wanted node in the list
    '''
    def get_node_value(self, index):
        if index < 0 or index > self.len-1:
            return
        cur, counter = self.head, 0
        while counter < index:
            cur = cur.next
            counter += 1
        return cur.data

    '''
    Replaces the value of a wanted indexed node
    ''' 
    def update_value(self, value, index):
        if index > self.len-1 or index < 0:
            return
        if index == 0:
            self.head.data = value
        elif index == self.len-1:
            self.tail.data = value
        else:
            to_rep = self.get_node(index)
            to_rep.data = value

    '''
    Inserts a node in a specific index of the list
    '''
    def insert_node(self, index, value):
        if index < 0 or index > self.len:
            return
        if index == 0:
            self.unshift_node(value)
        elif index == self.len:
            self.append_node(value)
        else:
            prev = self.get_node(index-1)
            next = prev.next
            new_node = self.Node(value)
            #Asignaciones de enlace
            prev.next = new_node
            new_node.prev = prev
            new_node.next = next
            next.prev = new_node
            self.len += 1

    '''
    Removes a eanted indexed node from the list
    '''
    def remove_by_index(self, index):
        if index < 0 or index > self.len-1:
            return
        if index == 0:
            self.remove_head()
        elif index == self.len-1:
            self.pop()
        else:
            temp = self.get_node(index)
            next = temp.next
            prev = temp.prev
            #Asignaciones de enlace
            prev.next = next
            next.prev = prev
            self.len -= 1

    '''
    Puts the list in reverse order
    '''
    def reverse(self):
        arr = []
        if self.len <= 1:
            cur = self.head
            if cur != None:
                arr.append(round(cur.data ** (1/2), 2))
            return
        for i in range(self.len):
            cur = self.head
            arr.insert(0, round(cur.data ** (1/2), 2))
            self.insert_node(self.len-i, cur.data)
            self.remove_head()
        print(arr, self.len)

