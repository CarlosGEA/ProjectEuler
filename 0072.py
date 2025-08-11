"""
Name : Counting Fractions
Date created : 11-08-2025
"""

import math

TRIAL = 8
CHALLENGE = 1_000_000


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def main():

    res = 0
    primes = sieve(CHALLENGE)

    for n in range(1, CHALLENGE + 1):
        if n % 1000 == 0:
            print(n, res)
            
        if n in primes:
            res += n - 1

        else:
            for i in range(1, n):
                if gcd(i, n) == 1:
                    res += 1

    print(res)

    return None


if __name__ == "__main__":
    main()


# 1 - 0
# 2 - 1
# 3 - 3
# 4 - 5
# 5 - 9
# 6 - 11
# 7 - 17
# 8 - 21
# 9 - 27
# 10 - 31
# 11 - 41
# 12 - 45
# 13 - 57
# 14 - 63
