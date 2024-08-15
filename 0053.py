"""
Name : Combinatronics Selection
Date created : 14-08-2024
"""

import math

max = 100
limit = 1_000_000


def main():

    count = 0
    for i in range(max + 1):
        for j in range(i + 1):
            if math.comb(i, j) >= limit:
                count += 1
    print(f"The number of coefficients more than {limit:.1e} for combinations up to 100 is {count}")
    return None


if __name__ == "__main__":
    main()
