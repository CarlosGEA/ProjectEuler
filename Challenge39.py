"""
Name : Integer Right Triangles
Date created : 19-07-2024
"""

from collections import defaultdict


def getTriplets():
    triplets = defaultdict(set)
    for n in range(1, 100): 
        for m in range(2, 100):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a**2 + b**2 == c**2 and a > 1:
                triplets[a + b + c].add(c)
                k = 1
                while (a + b + c) * k < 1000:
                    k += 1
                    triplets[(a + b + c) * k].add(c * k)
    return triplets


def main():

    triplets = getTriplets()
    triplets = dict((k, v) for k, v in triplets.items() if k < 1000)
    max_triplets = 0
    p = 0
    for key, val in triplets.items():
        if len(val) > max_triplets:
            max_triplets = len(val)
            p = key
    print(
        f"The value of p for which the number of pythagorean triplets is maximised is {p} with 'c' values of {triplets[p]} "
    )
    return None


# 401,399,40
# 394,390, 56
# 375,360,105
# 370,350,120
# 364,336,140
# 357,315,168
# 350,280,210
# 348,252,240

if __name__ == "__main__":
    main()
