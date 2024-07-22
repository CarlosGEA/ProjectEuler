"""
Name : 
Date created : 21-07-2024
"""

import math

# From reading online this is more of a brute force method


def generatePentagonal(n):
    return int(n * (3 * n - 1) / 2)


def isPentagonal(num):
    return math.isqrt(1 + 24 * num) and ((1 + math.sqrt(1 + 24 * num)) % 6 == 0)


def main():
    ans = 0
    k = 2
    while not ans:
        j = 1
        pk = generatePentagonal(k)
        while j < k:
            pj = generatePentagonal(j)
            if isPentagonal(pk + pj) and isPentagonal(pk - pj):
                ans = pk - pj
            j += 1
        k += 1
    print(ans)
    return None


if __name__ == "__main__":
    main()
