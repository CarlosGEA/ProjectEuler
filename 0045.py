"""
Name : Triangular, Pentagonal, and Hexagonal
Date created : 22-07-2024
"""

import math
import itertools


# def generateTriangle():
#     t = 1
#     d = 1
#     while True:
#         yield t
#         t += d
#         d += 1


def generateTriangle(n):
    return int(n * (n + 1) / 2)


def isPentagonal(num):
    return math.isqrt(1 + 24 * num) and ((1 + math.sqrt(1 + 24 * num)) % 6 == 0)


def isHexagonal(num):
    return math.isqrt(1 + 8 * num) and ((1 + math.sqrt(1 + 8 * num)) % 4 == 0)


def main():
    # for p in itertools.islice(generateTriangle(), 10):
    #     print(p)
    tph = 0
    n = 1
    while tph <= 40755:
        num = generateTriangle(n)
        if isPentagonal(num) and isHexagonal(num):
            tph = num
        n += 1
    print(num)

    return None


if __name__ == "__main__":
    main()
