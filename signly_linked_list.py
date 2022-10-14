class linked_list:
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tale = None
        self.len = 0
    
    """append a node to the end of the linked list"""
    def append_node(self, data):
        cur, node = self.head, self.Node(data)
        self.len += 1
        if self.head is None:
            self.head = node
            self.tale = node
            return
        while cur.next != None:
            cur = cur.next
        cur.next = node
        self.tale = node
       
    """displays the full linked list"""
    def print(self):
        cur, list = self.head, []
        while cur != None:
            list.append(cur.data)
            cur = cur.next
        print(list, self.len)

    """replaces a new node to the place of the head"""
    def unshift_node(self, data):
        cur, node = self.head, self.Node(data)
        self.len += 1
        if self.head is None:
            self.head = node
            self.tale = node
            return
        node.next = cur
        self.head = node

    """removes the first node (head) from the linked list"""
    def remove_head(self):
        if self.len > 0:
            self.len -= 1
            self.head = self.head.next
    
    """removes the last nide from the linked list"""
    def pop(self):
        if self.len <= 1:
            self.head = None
            self.len = 0
            return
        cur, prev = self.head, None
        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None
        self.tale = prev
        self.len -= 1

    """remove an specific value from the linked list"""
    def remove_by_value(self, data):
        cur, prev = self.head, None
        flag = False
        while cur.data != data:
            if cur.data == data:
                flag = True
            prev = cur
            cur = cur.next
        if flag:
            self.len -= 1
            prev.next = cur.next

    """returns a node from the linked list"""
    def get_node_value(self, index):
        if index > self.len-1 or index < 0:
            return 
        cur, count = self.head, 0
        while count < index:
            cur = cur.next
            count += 1
        return cur.data

    """returns a node value deppending in a index given"""
    def get_node(self, index):
        if index > self.len-1 or index < 0:
            return
        else:
            cur, counter = self.head, 0
            while counter < index:
                cur = cur.next
                counter += 1
            return cur

    """changes the value of any selected node in the linked list"""
    def update_value(self, value, index):
        if index > self.len-1 or index < 0:
            return
        if index == 0:
            self.head.data = value
        elif index == self.len-1:
            self.tale.data = value
        else:
            to_replace = self.get_node(index)
            to_replace.data = value

    """removes a node using x index"""
    def remove_by_index(self, index):
        if index < 0 or index > self.len-1:
            return
        if index == 0:
            self.remove_head()
        elif index == self.len-1:
            self.pop()
        else:
            to_del = self.get_node(index)
            prev = self.get_node(index-1)
            prev.next = to_del.next
            self.len -= 1
    
    """Inserts a valued-node in x index given by the user"""
    def insert_node(self, index, value):
        if index < 0 or index > self.len:
            return
        if index == 0:
            self.unshift_node(value)
        elif index == self.len:
            self.append_node(value)
        else:
            prev, new_node = self.get_node(index-1), Node(value)
            new_node.next = prev.next
            prev.next = new_node
            self.len += 1

    """Puts the linked list in a reverse order"""
    def reverse(self):
        if self.len <= 1:
            return
        else:
            counter = 0
            while counter < self.len-1:
                cur = self.head
                self.insert_node(self.len-counter, cur.data)
                self.remove_head()
                counter += 1





