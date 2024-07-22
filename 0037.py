"""
Name : Truncatable Primes
Date created : 15-07-2024
"""

import math

SIZE = 11


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


def truncateNumber(str_num):
    for i in range(1, len(str_num)):
        if not isPrime(int(str_num[i:])) or not isPrime(int(str_num[:-i])):
            return False
    return True


def main():
    trunc_primes = []
    num = 13
    while len(trunc_primes) < SIZE:
        str_num = str(num)
        if str_num[-1] == "7":
            num += 6
        elif str_num[-1] == "3":
            num += 4
        if not isPrime(int(str_num)):
            continue
        if truncateNumber(str_num):
            trunc_primes.append(int(str_num))
    print(f"Sum of fully truncatable primes is {sum(trunc_primes)}")
    return None


if __name__ == "__main__":
    main()
