import sys

class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    def __init__(self):
        self.head = None 
        self.tail = None
        self._size = 0


    def is_empty(self):
        return self._size==0


    def __len__(self):
        return self._size


    # Insert 'value' at the front of the list
    def insert_at_front(self, value):
        node = self.Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    

    #  insert value at the back of the linked list
    def insert_at_back(self, value):
        node = self.Node(value)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    

    # inserts value after key
    def insert_after(self, key, value):
        node = self.Node(value)

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
        return self.head.data #?


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
    def find(self, key):   #fix
        count = 0
        if self.is_empty():
            print ("List is empty")
            return False
        curr = self.head
        while curr != None and curr.data != key:
            count+=1            
            curr = curr.next
        if curr == None:
            return count
        return count


    # print all the items
    def printlist(self):
        if self.is_empty():
            print ("Nothing to show")
        else:
            curr = self.head
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.next
            print ("")
    

    def print_reverse(self):
        if self.is_empty():
            print ("Nothing to show")
        else:
            curr = self.tail
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.prev
            print("")


    def del_all(self):
        while(self.head!=None):
            node = self.head
            self.head = self.head.next
            node = None
        return "Deleted all"




if __name__ == '__main__':

    print("Instantiating a new list: ")
    L = DoublyLinkedList()
    print("Printing L: ", L)
    #X = L.Node('x')
    #print("X: ",X)
    print("The list is empty: ", L.is_empty())
    print("Length of list:", len(L))

    print("Inserting AAA, BBB, CCC and DDD\n")

    L.insert_at_front('AAA')
    L.insert_at_front("BBB")
    L.insert_at_back('CCC')
    L.insert_at_back('DDD')
    L.print_reverse()

    print("The list is empty: ",L.is_empty())
    print("Length of list:", len(L))
    print("Linked List: \n")
    L.printlist()

    print("Removing the element in the front and removing the element in the back")
    print(L.pop_front())
    print(L.pop_back())
    print("The list is empty: ", L.is_empty())
    print("Length of list:", len(L))
    print("Linked List: \n")
    L.printlist()

    print("EEE is not present in the list: ", end = " ")
    L.insert_after(2,'EEE')
    print(L.remove(4))

    print("Searching for 'EEE' in the list..")
    print(L.find('EEE'))   #print the number of occurences
    
    print(L.del_all())
    
    print(L.is_empty())