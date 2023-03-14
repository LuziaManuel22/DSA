
# FIFO Queue implementation using a Python list as
# its underlying storage.
class QueueADT:
    # Create an empty queue.
    def __init__(self):
        self.data = []
 
    # Add element e to the back of the queue
    def enqueue(self, e):
        self.data.insert(0, e)
 
    # Remove and return the element from the front of the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data.pop()
 
    # Return (but do not remove) the first element of the
    # queue. Raise exception if the queue is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data[-1]
 
    # Return True if the queue is empty.
    def is_empty(self):
        return len(self.data) == 0
 
    # Return the number of elements in the queue.
    def size(self):
        return len(self.data)
 
 
Q = QueueADT()
Q.enqueue("Q")
Q.enqueue("U")
Q.enqueue("E")
Q.enqueue("U")
Q.enqueue("E")
Q.peek()         # Q
Q.size()         # 5
Q.is_empty()     # False
Q.dequeue()      # Q
Q.dequeue()      # U
Q.dequeue()      # E
Q.dequeue()      # U
Q.dequeue()      # E
Q.is_empty()     # True
Q.size()         # 0
Q.peek()         # IndexError: Queue is empty