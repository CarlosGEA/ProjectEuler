"""
Name : Diophantine Equation
Date created : 04-08-2025
"""

import math

TRIAL = 8
CHALLENGE = 1001



def isSquare(num):
    return math.isqrt(num) ** 2 == num

def calcNewFraction(n, x, y):
    # in form y / (sqrt(n) - x)
    val = y / (math.sqrt(n) - x)
    a_term = int(math.floor(val))
    new_y = int((n - x * x) / y)
    new_x = (a_term * new_y) - x
    return a_term, new_x, new_y

def calcContinuedFraction(num):
    """
    In the form [x,y0,y1,y2...] which corresponds to sqrt(n) ~= x + 1 / (y0 + 1 / (y1 + 1 / (y2 + 1 / ...)))
    """

    seen = set()  # tuple of (a_term, minus_term, denominator)
    minus_term = math.floor(math.sqrt(num))
    a_notation = []

    denom = 1
    while True:
        new_terms = calcNewFraction(num, minus_term, denom)  # returns tuple of a_term, minus_term, denom
        if new_terms in seen:
            break
        seen.add(new_terms)
        a, minus_term, denom = new_terms
        a_notation.append(a)

    return minus_term, a_notation


def calcTruncatedFraction(start, a_terms, repeat):
    # [ ... , a, b ] = [ ... , a + 1/b ]

    numer = 0
    denom = 1
    if repeat:
        a_terms = a_terms + a_terms
    a_terms = a_terms[:-1]

    # print(start, a_terms)

    for a in a_terms:
        numer += (a * denom)
        numer, denom = denom, numer
    numer += (start * denom)

    return numer, denom


def main():

    """
    Diophantine Equation : x^2 - D * y^2 = 1
    Solved by finding continued fraction of sqrt(D)
    Continued fraction is of form [x,y0,y1,y2] ...
    If even number of y's then calculate x + 1 / (y0 + 1 / ...) up to y1
    If odd number of y's then calculate x + 1 / (y0 + 1 / ...), go through first period and end before second y2
    This gives a fraction a / b where a -> x and b -> y in the first line
    """

    # possibleD = [num for num in range(1, TRIAL) if not isSquare(num)]
    possibleD = [num for num in range(1, CHALLENGE) if not isSquare(num)]

    x_res = []
    for d in possibleD:
        start, a_terms = calcContinuedFraction(d)
        
        if len(a_terms) % 2 == 0:
            # Even period
            numerator, denominator = calcTruncatedFraction(start, a_terms, False)

        else:
            # Odd period
            numerator, denominator = calcTruncatedFraction(start, a_terms, True)

        x_res.append(numerator)

    max_x = max(x_res)
    D_val = possibleD[x_res.index(max_x)]
    print(f"The value of D in minimal solutions of x for which the largest value of x is obtained is {D_val}")

   
    return None


if __name__ == "__main__":
    main()