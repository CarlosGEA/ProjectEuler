"""
Name : Arranged Probability
Date created : 22-08-2025
"""

import math


def isPrime(n):
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


def pickTwo(x, n):
    return x / n * (x - 1) / (n - 1)


def main():

    while True:
        n = 10**12
        x = n // 2
        while pickTwo(x, n) < 0.5:
            while isPrime(x):
                x += 1
            x += 1
            print(x)
        if pickTwo(x, n) == 0.5:
            print(x, n, n - x)
            break

        while isPrime(n):
            n += 1
    # too much brute force
    
    return None


if __name__ == "__main__":
    main()
