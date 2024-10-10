"""
Name : Pandigital Prime
Date created : 20-07-2024
"""

import math
from itertools import permutations

# can reduce this by seeing that none of 1,2,3,5,6,8,9 digit pandigitals are prime so only need to check for 4 and 7


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


def isPandigital(str_num):
    if len(str_num) == int(max(str_num)):
        return True
    return False


def main():

    pandigit = "123456789"
    highest = 0
    for i in [4, 7]:
        for c in permutations(pandigit, i):
            num = int("".join(c))
            if isPrime(num) and isPandigital(str(num)) and num > highest:
                highest = num

    print(f"The largest pandigital prime is {highest}")

    return None


if __name__ == "__main__":
    main()
