"""
Name : Totient Permutation
Date created : 10-08-2025
"""

from collections import Counter

CHALLENGE = 1_000_000_0


def isPermutation(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))


def main():

    res = 0
    ratio = float("inf")

    # only check odd numbers as even will have too high ratio

    for num in range(2, CHALLENGE):
        new_ratio = 2
        if new_ratio < ratio:
            res = num
            ratio = new_ratio

        # print(num)
    print(f"Current poss is {87109/79180}")

    print(f"The smallest ratio is {new_ratio} for number {res}")
    return None


if __name__ == "__main__":
    main()
