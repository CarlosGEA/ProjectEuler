"""
Name : Lexicographic Permutations
Date created : 02-07-2024
"""

from itertools import permutations

TRIAL = 3
CHALLENGE = 10


def add_perm(nums):

    return nums


def main():
    n = 1000000
    lex = "".join((map(str, range(CHALLENGE))))

    perms = ["".join(p) for p in permutations(lex)]
    print(f"The answer is {perms[n-1]}")

    return None


if __name__ == "__main__":
    main()
