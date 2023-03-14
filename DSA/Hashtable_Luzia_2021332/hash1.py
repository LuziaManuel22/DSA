class MyHashTable:

 def __init__(self, capacity):
    self.capacity = capacity
    self.slots = [None] * self.capacity

def __str__(self):
    return str(self.slots )

def __len__(self):
    count = 0
    for i in self.slots:
        if i != None:
            count += 1
    return count

def hash_function(self, key):
    i = key % self.capacity
    return i

def insert(self, key):
    slot = self.hash_function(key)
    if key in self.slots[slot]:
        return -2
    elif key in self.slots[slot] == False:
        return -1
    else:
        self.slots[slot].append(key)
        return slot

    x = MyHashTable(2)

    print("Add 3, return:", x.insert(3))
    print("Hashtable:", x)
    print("Add 3, return:", x.insert(3))  
    print("Hashtable:", x)
