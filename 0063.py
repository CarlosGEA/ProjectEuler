"""
Name : Powerful Digit Counts
Date created : 08-03-2025
"""

import math, time

MAX = 310


def main():

    start = time.time()

    res = []
    count = 0
    for num_len in range(1, MAX):
        number = math.floor(math.pow(10, num_len - 1) ** (1 / num_len))

        while number <= 9:
            calc = int(math.pow(number, num_len))
            if len(str(calc)) == num_len:
                count += 1
                res.append([number, num_len, calc])
            number += 1

    print(f"The number of n-digit positive integers exist which are also an n'th power is {count}")
    print(f"These numbers are {res}")

    end = time.time()
    print(f"Time: {end-start}")

    return None


if __name__ == "__main__":
    main()
