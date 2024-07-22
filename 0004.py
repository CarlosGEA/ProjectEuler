"""
Name : Largest Palindrome Product
Date created : 28-05-2024
"""

TWOP = 9009


def calculate_products(n):
    """
    n - number of digits of the two factors of the palindrome
    """

    start_num = 10**n - 1
    end_num = 10 ** (n - 1)
    product = 0
    factors = []
    while start_num > end_num:
        for i in range(end_num, start_num + 1):
            prod = i * start_num
            if check_palindrome(prod):
                if prod > product:
                    product = prod
                    factors = [start_num, i]
        start_num -= 1
    return product, factors

def check_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def main():
    n = 2
    pal, factors = calculate_products(3)
    print(f"The largest palindrome made from the product of two {n}-digit numbers is {pal}={factors[0]}x{factors[1]}")
    print(f"The largest palindrome made from the product of two 2-digit numbers should be {TWOP}")

    return None


if __name__ == "__main__":
    main()
