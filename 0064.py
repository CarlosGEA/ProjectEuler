"""
Name : Odd Period Square Root
Date created : 08-03-2025
"""

import math

TRIAL = 14
CHALLENGE = 10_000


def calc(n, x, y):
    # in form y / (sqrt(n) - x)
    val = y / (math.sqrt(n) - x)
    a_term = int(math.floor(val))
    new_y = int((n - x * x) / y)
    new_x = (a_term * new_y) - x
    return a_term, new_x, new_y


def main():

    res = 0
    for num in range(1, CHALLENGE):
        seen = set()  # tuple of (a_term, minus_term, denominator)
        if math.isqrt(num) ** 2 == num:
            continue

        minus_term = math.floor(math.sqrt(num))
        denom = 1
        while True:
            new_terms = calc(num, minus_term, denom)  # returns tuple of a_term, minus_term, denom
            if new_terms in seen:
                if len(seen) % 2 != 0:
                    res += 1
                break

            seen.add(new_terms)
            _, minus_term, denom = new_terms

    print(f"The number of odd period irrational square roots less than {CHALLENGE} is {res}")
    # print(f"The number of odd period irrational square roots less than {TRIAL} is {res}")

    return None


if __name__ == "__main__":
    main()
