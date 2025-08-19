"""
Name : Digit Factorial Chains
Date created : 19-08-2025
"""

import math
from functools import lru_cache


CHALLENGE = 1_000_000

# FACTORIALS = {i: math.factorial(i) for i in range(0, 10)}


def nextNum(n):
    str_n = str(n)
    res = 0
    for c in str_n:
        res += math.factorial(int(c))
        # res += FACTORIALS[int(c)]

    return res


def main():

    links = {}

    for num in range(1, CHALLENGE + 1):
        current = num
        while current not in links:
            next_num = nextNum(current)
            links[current] = next_num
            current = next_num

    res = 0
    for num in range(1, CHALLENGE + 1):
        chain_len = 0
        cur = num
        seen = set()
        while cur not in seen:
            chain_len += 1
            seen.add(cur)
            cur = links[cur]

        if chain_len == 60:
            res += 1

    print(f"The number of chains of length 60 is {res}")

    return None


if __name__ == "__main__":
    main()
