"""
Name : Circular Primes
Date created : 14-07-2024
"""

import math
import itertools

TEST = 100
CHALLENGE = 1_000_000


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


def numberCombinations(num):
    nums = [num]
    str_num = str(num)
    for i in range(1, len(str_num)):
        num = str_num[i:] + str_num[:i]
        nums.append(int(num))
    return nums


def main():
    circular_primes = {2}
    for num in range(3, CHALLENGE, 2):
        if num in circular_primes:
            continue
        nums = numberCombinations(num)
        if all(isPrime(x) for x in nums):
            circular_primes.update(nums)
    circular_primes = sorted(list(circular_primes))
    # print(circular_primes)
    
    print(f"There are {len(circular_primes)} circular primes below {CHALLENGE}")
    return None


if __name__ == "__main__":
    main()
