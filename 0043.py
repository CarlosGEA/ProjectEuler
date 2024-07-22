"""
Name : Sub-string Divisibility
Date created : 21-07-2024
"""

import collections
from itertools import permutations


NUM_DIV = [2, 3, 5, 7, 11, 13, 17]


def checkCondition(num):
    for idx, elem in enumerate(NUM_DIV[::-1]):
        split_num = int(num[7 - idx : 10 - idx])
        if split_num % elem == 0:
            continue
        else:
            return False
    return True


def main():

    pandigit = "0123456789"
    num_div_pandigits = []

    for c in permutations(pandigit, len(pandigit)):
        str_num = "".join(c)
        if checkCondition(str_num):
            num_div_pandigits.append(int(str_num))
    print(f"The answer is {sum(num_div_pandigits)}")
    return None


if __name__ == "__main__":
    main()
