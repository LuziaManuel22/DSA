def readPolynomialFromUser():
    number_polynomials = int(input())
    P=[0 for i in range(number_polynomials)]
    for i in range(0,number_polynomials):
        index_p,index_c = input().split(' ')
        P[int(index_p)] = int(index_c)
    return P


def computePolynomialSum(A,B):
    if(len(A)>=len(B)):
        polynomials_sum=[0 for i in range(len(A))]
        for i in range(0,len(A)):
            if(i>=len(B)):
                B.append(0)
            polynomials_sum[i]=A[i]+B[i]
        return polynomials_sum


    return -1

