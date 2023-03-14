#Requires that module ‘array’ be imported

# Python program to create an Array

# importing "array" to work with arrays

import array as ARR

# creating an array with integer type

A = ARR.array('i', [1, 2, 3])

print(A)

print()

# creating an array with float type

B = ARR.array('d', [2.5, 3.2, 3.3])

print(B)

print()

#Output:

array=('i', [1, 2, 3])

array=('d', [2.5, 3.2, 3.3])