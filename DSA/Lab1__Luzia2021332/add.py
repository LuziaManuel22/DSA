def add(A, B, m, n):
 
    size = max(m, n);
    sum = [0 for i in range(size)]
 
    # Initialize the product polynomial
     
    for i in range(0, m, 1):
        sum[i] = A[i]
 
    # Take ever term of first polynomial
    for i in range(n):
        sum[i] += B[i]
 
    return sum
 
# A utility function to print a polynomial
def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
 