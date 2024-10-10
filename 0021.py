"""
Name : Amicable Numbers
Date created : 05-06-2024
"""

import math


def getFactors(n):
    factor_list = [1]
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            factor_list.extend([i, n // i])
    return factor_list


def main():
    amicable_pairs = []
    for num in range(1, 10000):
        factor_sum = sum(getFactors(num))
        if num == sum(getFactors(factor_sum)) and num != factor_sum and num not in amicable_pairs:
            amicable_pairs.extend([num, factor_sum])
    print(f"The sum of all amicable numbers is {sum(amicable_pairs)}")
    return None


if __name__ == "__main__":
    main()
