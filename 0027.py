"""
Name : Quadratic Primes
Date created : 04-07-2024
"""

import math


def quadraticFormula(n, a, b):
    return n * n + a * n + b


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(6, math.floor(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % (x + 1) == 0:
            return False
    return True


def main():

    max_count = 0
    prod = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            i = 0
            val = quadraticFormula(i, a, b)
            while is_prime(val):
                i += 1
                val = quadraticFormula(i, a, b)
            if i > max_count:
                max_count = i
                prod = a * b

    print(max_count, prod)

    return None


if __name__ == "__main__":
    main()
