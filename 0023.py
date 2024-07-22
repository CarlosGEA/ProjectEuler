"""
Name : Non-Abundant Sums
Date created : 12-06-2024
"""

import math

MAX = 28123


def getFactors(n):
    factor_list = [1]
    val = math.ceil(math.sqrt(n))
    for i in range(2, val):
        if n % i == 0:
            factor_list.extend([i, n // i])
    if val**2 == n and n != 1:
        factor_list.append(val)
    return factor_list


def isAbundant(num):
    return sum(getFactors(num)) > num


def main():
    abundant_nums = []
    for i in range(1, MAX + 1):
        if isAbundant(i):
            abundant_nums.append(i)

    print(abundant_nums[:20])

    final_nums = list(range(1, MAX + 1))
    two_sums = sorted(
        set(
            abundant_nums[i] + abundant_nums[j]
            for i in range(len(abundant_nums))
            for j in range(i, len(abundant_nums))
        )
    )
    two_sums[:] = [x for x in two_sums if x <= MAX]
    for i in two_sums:
        if i in final_nums:
            final_nums.remove(i)
    print(f"The final answer is {sum(final_nums)}")
    return None


if __name__ == "__main__":
    main()
