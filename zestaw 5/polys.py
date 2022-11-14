# ZADANIE 5.3
# Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach. 
# Wielomian będzie reprezentowany przez listę swoich współczynników, 
# np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. 
# Napisać kod testujący moduł polys.

def add_poly(poly1, poly2):         # poly1(x) + poly2(x)
    poly3 = [0 for x in range(max(len(poly1), len(poly2)))]

    for x in range(max(len(poly1), len(poly2))):
        if x < len(poly1):
            poly3[x] += poly1[x]
        if x < len(poly2):
            poly3[x] += poly2[x]

    return poly3

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    poly3 = [0 for x in range(max(len(poly1), len(poly2)))]

    for x in range(max(len(poly1), len(poly2))):
        if x < len(poly1):
            poly3[x] += poly1[x]
        if x < len(poly2):
            poly3[x] -= poly2[x]
    
    return poly3

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    poly3 = [0 for x in range(len(poly1) + len(poly2) - 1)]

    for x in range(len(poly2)):
        for y in range(len(poly1)):
            poly3[x+y] += poly2[x]*poly1[y]

    while True:
        if len(poly3) > 0 and poly3[-1] == 0:
            poly3.pop()
        else:
            break
    return poly3

def is_zero(poly):                  # bool, [0], [0,0], itp.
    for x in range(len(poly)):
        if poly[x] != 0: 
            return False
    return True

def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    while True:
        if len(poly1) > 0 and poly1[-1] == 0:
            poly1.pop()
        else:
            break
    while True:
        if len(poly2) > 0 and poly2[-1] == 0:
            poly2.pop()
        else:
            break

    return poly1 == poly2


def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    result = poly[0]

    for x in range(1, len(poly)):
        result += poly[x]*x0**x

    return result

def combine_poly(poly1, poly2):         # poly1(poly2(x)), trudne!
    result = [0]
    for x, y in enumerate(poly1):
        result = add_poly(result, [y * i for i in pow_poly(poly2, x)])
    return result

def pow_poly(poly, n):            # poly(x) ** n
    poly2 = poly
    for _ in range(n-1):
        poly2 = mul_poly(poly2, poly)

    return poly2
    

def diff_poly(poly):                   # pochodna wielomianu
    diff = [0 for _ in range(len(poly)-1)]

    for x in range(len(diff)):
        diff[x] = poly[x+1]*(x+1)
    
    return diff