"""
Name : Digit Factorials
Date created : 14-07-2024
"""

import math

FACTORIALS = {digit: math.factorial(digit) for digit in range(10)} # Updated to not recalculate this
MAX = 7 * FACTORIALS[9]


def FactorialSum(num):
    fsum = 0
    for digit in str(num):
        fsum += FACTORIALS[int(digit)]
    return fsum


def main():

    factorial_nums = []
    for num in range(10, MAX):
        factorial_sum = FactorialSum(num)
        if factorial_sum == num:
            factorial_nums.append(num)
    print(sum(factorial_nums))

    return None


if __name__ == "__main__":
    main()
