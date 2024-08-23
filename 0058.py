"""
Name : Spiral Primes
Date created : 16-08-2024
"""

import math

LIMIT = 0.1


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


def main():

    prime_ratio = 0.6
    side_length = 3
    primes = 3
    nums = 5
    highest_num = 9
    while prime_ratio > 0.1:
        side_length += 2

        diff = side_length - 1
        new_nums = [highest_num + diff * i for i in range(1, 5)]
        highest_num = new_nums[-1]
        primes += sum(1 for num in new_nums if isPrime(num))

        nums += 4
        prime_ratio = primes / nums

    print(f"The answer is {side_length} with ratio {prime_ratio}")
    return None


if __name__ == "__main__":
    main()
