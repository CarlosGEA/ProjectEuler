"""
Name : Consecutive Prime Sum
Date created : 29-07-2024
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


    nums = {}
    for n in range(2, 7):
        consecutive_sum = 0
        consectuive_nums = 0
        while consecutive_sum + n < 1_000_000:
            if isPrime(n):
                consecutive_sum += n
                consectuive_nums += 1
                if isPrime(consecutive_sum):
                    nums[consectuive_nums] = consecutive_sum
            n += 1
    print(f"The largest sum of consecutive primes below 1e6 is {nums[max(nums)]}")
    
    return None


if __name__ == "__main__":          
    main()