"""
Name : Special Pythagorean Triplet
Date created : 31-05-2025
"""

import math

CHALLENGE = 1000
TRIAL = 12


def findTriplet(num, triplets):
    for ts in triplets:
        if sum(ts) == num:
            return ts
    return None


def getTriplets():
    triplets = []
    for n in range(1, 100):
        for m in range(2, 100):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a**2 + b**2 == c**2:
                triplets.append([a, b, c])
    return triplets


def main():

    triplets = getTriplets()
    sol = findTriplet(CHALLENGE, triplets)

    print(f"The triplets summing to {CHALLENGE} are {sol}")
    print(f"Their product is {math.prod(sol)}")
    return None


if __name__ == "__main__":
    main()

# The triplets summing to 1000 are [-9000, 950, 9050]
# Their product is -77377500000 # also an answer
