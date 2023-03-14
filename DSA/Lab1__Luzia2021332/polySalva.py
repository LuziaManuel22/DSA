def F(P, x):
    result = 0
    for exponent, coeficient in enumerate(P):
        result += coeficient * x ** exponent
    return result