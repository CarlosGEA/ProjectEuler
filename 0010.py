"""
Name : Sum of Primes
Date created : 31-05-2024
"""

import math

TRIAL = 8
CHALLENGE = 2e6


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

    ans = 17
    primes = []
    n = 1
    while n < CHALLENGE:
        n += 1
        if is_prime(n):
            primes.append(n)
    ans = sum(primes)

    print(f"The sum of all primes below {TRIAL} is 17")
    print(f"The sum of all primes below {CHALLENGE:.1e} is {ans}")

    return None


if __name__ == "__main__":
    main()
