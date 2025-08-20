"""
Name : Square Root Digital Expansion
Date created : 20-08-2025
"""

import math


def Newton(n):

    trial = math.isqrt(n * 10 ** (2 * (101 - len(str(n)))))
    return trial


def main():

    squares = set(i**2 for i in range(11))
    # sqrt 2 = 1.41111 : sum of first 100 numbers is 475
    # calculate this for the first 100 natural numbers with irrational roots i.e. exclude 4,9...
    # sum each one

    res = 0
    for num in range(100):
        if num in squares:
            continue

        root = Newton(num)
        root_sum = sum(int(i) for i in str(root)[:100])

        res += root_sum

    print(res)

    return None


if __name__ == "__main__":
    main()
