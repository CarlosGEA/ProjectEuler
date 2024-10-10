"""
Name : Highly Divisible Triangular Number
Date created : 02-06-2024
"""

import math

TRIAL = 5
CHALLENGE = 500


def factors(num):

    total = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += 1
    total *= 2
    if num == i * i:
        total -= 1
    return total


def main():

    number = 0
    triangle_number = 0
    count = 1

    while number <= CHALLENGE:
        triangle_number += count
        number = factors(triangle_number)
        count += 1

    print(f"The first triangle number to have over {CHALLENGE} divisors is {triangle_number}")
    return None


if __name__ == "__main__":
    main()
