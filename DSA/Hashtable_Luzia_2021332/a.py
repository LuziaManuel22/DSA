"""Hash Table
THIS HASH TABLE ASSUMES THAT YOU ARE PUTTING UNIQUE KEYS WHEN YOU...
...CALL put FUNCTION, 
MAKE AN UPDATE FUNCTION IF YOU ARE PUTTING REPEATED KEYS

Included:
	- hash / rehash (using linear probe)
	- load factor
    - put
	- get

Not included:
	- Get prime/ Check prime
    - Resize
    - Update
    and more...
"""
import fractions
class HashTable:
    def __init__(self, size):
        self._size = size
        self._used = 0
        self._keys = [None]*size
        self._values = [None]*size
        
    def hash_function(self, key):
        return (key % self._size)
    
    def rehash(self, old_key):
        return self.hash_function(old_key + 1) # Linear Probe
    
    def load_factor(self):
        return fractions.Fraction(self._used, self._size)
    
    def full(self):
        return self.load_factor() == 1
    
    def put(self, key, value):
        if self.full():
            return "Full"
        
        # There is empty space
        # Get digest
        digest = self.hash_function(key)
        
        # Resolve collisions
        # Rehash if not empty or key does not exist
        while self._keys[digest] is not None and self._keys[digest] != key:
            digest = self.rehash(digest)
            
        # Don't put if key already exists
        if self._keys[digest] == key:
            return "Exists"
        
        # Finally can put in empty space
        else:
            self._keys[digest] = key
            self._values[digest] = value
            self._used += 1 # update used space counter
            return "Entered"
            
    def get(self, key):
        # Get digest
        digest = self.hash_function(key)
        
        # Within the range of the total space
        for _ in range(self._size):
            if self._keys[digest] != key:
                digest = self.rehash(digest)
            else:
                return self._values[digest]
        
        # Not found
        return "Not found"
        
# Test
from randstr import randstr
from random import randint
def HT_Test(HT):
    print(f">>> HashTable:")
    # Make keys and values
    r = randint(8, 15)
    keys = [randint(10, 100) for _ in range(r)]
    vals = list(randstr(len(keys)))
    print(f"Keys to enter: {keys}",
          f"Vals to enter: {vals}",
          f"Key-value pair: {list(zip(keys, vals))}",   # display one list with key-value pair
          sep = "\n", end = "\n\n")
    
    # Initiate Hash Table
    H = HT(len(keys) - 2)
    
    # Put the key-value pair into Hash Table
    print("Put:")
    for i in range(len(keys)):
        key, val = keys[i], vals[i]
        print(f"Key: {key}",
              f"Status: {H.put(key, val)}",
              f"Load factor: {H.load_factor()}", 
              sep = " | ")
    print()
    print(f"Keys entered: {H._keys}",
          f"Values entered: {H._vals}", 
          sep = "\n", end = "\n\n")
    
    # Get the values in Hash Table for each corresponding key
    print("Get:")
    for key in keys:
        print(f"Key: {key}",
              f"({H.get(key)})",
              sep = " | ")