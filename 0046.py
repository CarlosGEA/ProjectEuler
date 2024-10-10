"""
Name : Goldbach's Other Conjecture
Date created : 22-07-2024
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


def main():
    double_square = [2 * n * n for n in range(1, 30)]
    possible_nums = set()
    scn = 0
    n = 1
    while not scn:
        if isPrime(n):
            for sq in double_square:
                possible_nums.add(sq + n)
        elif n % 2 != 0 and n not in possible_nums and n != 1:
            scn = n
        n += 1
    print(f"The smallest composite number not finding condition is {scn}")
    return None


if __name__ == "__main__":
    main()
