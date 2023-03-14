# LIFO Stack implementation using a linked list 
# as its underlying storage
class LinkedListStack:
    # ----------------------Nested Node Class ----------------------
 
    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e
            self.next = None   # reference to the next Node
 
# ---------------------- stack methods -------------------------
    # Create an empty stack
    def __init__(self):
        self._size = 0
        # reference to head node (top of stack)
        self.head = None
 
    # Add element e to the top of the stack.
    def push(self, e):
        # New node inserted at Head
        newest = self.Node(e)
        newest.next = self.head
        self.head = newest
        self._size += 1
 
    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
 
        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1
 
        return elementToReturn
 
    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.element
 
    # Return True if the stack is empty.
    def is_empty(self):
        return self._size == 0
 
    # Return the number of elements in the stack.
    def size(self):
        return self._size
 
 
LLS = LinkedListStack()
LLS.push("L")
LLS.push("L")
LLS.push("S")
LLS.push("T")
LLS.push("A")
LLS.push("C")
LLS.push("K")
LLS.peek()       # K
LLS.size()       # 7
LLS.is_empty()   # False
LLS.pop()        # K
LLS.pop()        # C
LLS.pop()        # A
LLS.pop()        # T
LLS.pop()        # S
LLS.pop()        # L
LLS.pop()        # L
LLS.is_empty()   # True
LLS.size()       # 0
LLS.peek()       # IndexError: Stack is empty