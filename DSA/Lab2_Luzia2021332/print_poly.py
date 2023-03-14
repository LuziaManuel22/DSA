def Print_Poly(d, coeffs):
    i = d - 1
    term = ""
    for c in coeffs:
        
        if i > 0:
            if i == 1:
                if c > 0:
                    term = term + " + {0} x".format(c)
                else:
                    term = term + " - {0} x".format(abs(c))
            else:
                term =  term + "{0} x^{1}".format(c, i)
        else:
            if c > 0:
                term = term + " + {0}".format(c)
            else:
                term = term  + " - {0}".format(abs(c)) 
        i = i - 1
        
    print(term)
    
d = int(input(""))
coe = []
for i in range(d):
    coe.append(int(input("")))
    
Print_Poly(d, coe)