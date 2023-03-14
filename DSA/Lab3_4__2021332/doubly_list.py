
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    # Insert 'value' at the front of the list
    def insert_at_front(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
     
    #  insert value at the back of the linked list
    def insert_at_back(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
           self.tail.next = node
           node.prev = self.tail
           self.tail = node
    
    # inserts value after key
    def insert_after(self, key, value):
        node = Node(value)

        # find the position of key
        curr = self.head
        while curr != None and curr.data != key:
            curr = curr.next
        if curr == None:
            print ("Key not found")
            return
        if curr.next == None:
            curr.next = node
            node.prev = curr
            self.tail = node 
        else:
            next_node = curr.next
            curr.next = node
            node.prev = curr
            node.next = next_node
            next_node.prev = node

    # returns the data at first node 
    def top_front(self):
        if self.is_empty():
            print ("List is empty")
            return
        return self.head.data

    # returns the data at last node 
    def top_back(self): 
        if self.is_empty():
            print ("List is empty")
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        return curr.data

    # removes the item at front of the linked list and return 
    def pop_front(self):
        if self.is_empty():
            print ("List is empty")
            return
        next_node = self.head.next
        if (next_node != None):
            next_node.prev = None
        item = self.head.data
        self.head = next_node
        return item

    # remove the item at the end of the list and return 
    def pop_back(self):
        if self.is_empty():
            print ("List is empty")
            return

        item = self.tail.data
        prev = self.tail.prev

        if prev != None:
            prev.next = None

        self.tail.prev = None
        self.tail = prev

        return item

    # removes an item with value 'key'
    def remove(self, key):
        if self.is_empty():
            print ("List is empty")
            return

        # find the position of the key
        curr = self.head
        while curr != None and curr.data != key:
            curr = curr.next
        if curr == None:
            print ("key not found")
            return

        # if curr is head, delete the head
        if curr.prev == None:
            self.pop_front()
        elif curr.next == None: # if curr is last item
            self.pop_back()
        else: #anywhere between first and last node
            next_node = curr.next
            prev_node = curr.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            curr.next = None 
            curr.prev = None
            curr = None

    # check if the key is in the list
    def find(self, key):
        if self.is_empty():
            print ("List is empty")
            return False
        curr = self.head
        while curr != None and curr.data != key:
            curr = curr.next
        if curr == None:
            return False
        return True

    # check if the list is empty
    def is_empty(self):
        return self.head == None

    # print all the items
    def printlist(self):
        if self.is_empty():
            print ("Nothing to display")
        else:
            curr = self.head
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.next
            print ("")
    
    def print_reverse(self):
        if self.is_empty():
            print ("Nothing to display")
        else:
            curr = self.tail
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.prev
            print ("")

   

if __name__ == '__main__':
    list = DoublyLinkedList()
    list.insert_at_front('BBB')
    list.insert_at_front('AAA')
    list.insert_at_back('CCC')
    list.insert_at_back('DDD')
    list.printlist()
    list.print_reverse()
    #list.pop_front()
    #list.printlist()
    #list.pop_back()
    #list.printlist()
  