"""
Name : Ordered Fractions
Date created : 11-08-2025
"""

TRIAL = 8
CHALLENGE = 1_000_000


def main():

    target = 3 / 7
    cur = 0
    res = [0, 0]
    # for n in range(TRIAL + 1):
    for n in range(CHALLENGE + 1):
        # print(n, cur)
        for num in range(res[0], n):
            frac = num / n
            if frac < target and frac > cur:
                cur = frac
                res = [num, n]
            if frac > target:
                break

    print(f"The number to the left of 3/7 is {res[0]}/{res[1]}")

    return None


if __name__ == "__main__":
    main()
