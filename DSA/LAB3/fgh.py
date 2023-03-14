class LinkedListQueue:
  # ----------------------Nested Node Class ----------------------
    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e    
            self.next = None   # reference to the next Node
 
# ---------------------- queue methods -------------------------
    # create an empty queue
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None
 
    # Add element e to the back of the queue.
    def enqueue(self, e):
        newest = self.Node(e)
 
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self._size += 1
 
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
 
        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
 
        return elementToReturn
 
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.head.element
 
    def is_empty(self):
        return self._size == 0
 
    def size(self):
        return self._size
 
 
LLQ = LinkedListQueue()
LLQ.enqueue("L")
LLQ.enqueue("L")
LLQ.enqueue("Q")
LLQ.enqueue("U")
LLQ.enqueue("E")
LLQ.enqueue("U")
LLQ.enqueue("E")
LLQ.peek()         # L
LLQ.size()         # 7
LLQ.is_empty()     # False
LLQ.dequeue()      # L
LLQ.dequeue()      # L
LLQ.dequeue()      # Q
LLQ.dequeue()      # U
LLQ.dequeue()      # E
LLQ.dequeue()      # U
LLQ.dequeue()      # E
LLQ.is_empty()     # True
LLQ.size()         # 0
LLQ.peek()         # IndexError: Queue is empty