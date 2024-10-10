"""
Name : Pandigital Products
Date created : 12-07-2024
"""

"""
Pandigital products must contain only digits 1-9 once and must be in the form x * y = z
This means any product of 5 or more digits must have been made from at least 5 other digits which would imply duplicate digits (1-9  is only 9)
Max products to check are 4 digits and must not contain 0 or be prime so can immediately eliminate those.
"""
import math

MAX = 99999


def uniqueDigits(str_num):

    if len(str_num) == len(set(str_num)):
        return True
    return False


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


def panFactors(n):
    """
    Gets factors not including 1 and itself, if you want them make factor_list = [1, n]
    """
    pan_factors = []
    val = math.ceil(math.sqrt(n))
    for i in range(2, val):
        if n % i == 0:
            if uniqueDigits(str(n) + str(i) + str(n // i)):
                pan_factors.append([i, n // i])
    return pan_factors


def main():
    check = list(map(str, range(1, 10)))
    pan_nums = set()
    factor_nums = []
    for num in range(2, 9999):
        str_num = str(num)
        if not uniqueDigits(str_num) or "0" in str_num or isPrime(num):
            continue  # if a number contains multiple of same digit, a zero or is prime it skips over it
        pan_factors = panFactors(num)
        for factors in pan_factors:
            str_all = "".join(map(str, factors)) + str_num
            if all(x in str_all for x in check):
                pan_nums.add(num)
                factor_nums.append(factors)

    print(f"The sum of all Pandigits containing 1-9 is {sum(pan_nums)}")

    return None


if __name__ == "__main__":
    main()
