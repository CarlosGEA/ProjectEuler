"""
Name : 10001st Prime
Date created : 30/05/2024
"""

import math

TEST = 6
CHALLENGE = 10001


def prime(nth):
    primes = [2]
    i = 2
    while len(primes) < nth:
        for num in range(2, i):
            if i % num == 0:
                break
            elif num == i - 1 and i not in primes:
                primes.append(i)
        i += 1
    return primes


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

    # sol = prime(TEST)
    # primes = prime(CHALLENGE)
    # sol = primes[-1]
    seen = 0
    n = 1
    while seen < CHALLENGE:
        n += 1
        if is_prime(n):
            seen += 1
    print(n)

    print(f"Prime number {TEST} is 13.")
    # print(f"My prime number {CHALLENGE} is {sol}.")

    return None


if __name__ == "__main__":
    main()
