"""
Name : Singular Integer Right Triangles
Date created : 19-08-2025
"""

import numpy as np
from collections import defaultdict
import math

CHALLENGE = 1_500_000
TRIAL = 48  # 6


def gen_prim_pyth_trips(limit=None):
    u = np.mat(" 1  2  2; -2 -1 -2; 2 2 3")
    a = np.mat(" 1  2  2;  2  1  2; 2 2 3")
    d = np.mat("-1 -2 -2;  2  1  2; 2 2 3")
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit // prim[2]):
            yield i
            i = i + prim


def main():

    triples = list(gen_all_pyth_trips((CHALLENGE // 2)))
    lengths = defaultdict(int)

    print(len(triples))
    for trip in triples:
        length = np.sum(trip)
        if length <= CHALLENGE:
            lengths[length] += 1

    res = 0
    for counts in lengths.values():
        if counts == 1:
            res += 1

    """Quicker method for generating the triples"""
    # lengths = defaultdict(set)

    # for m in range(2, int(math.sqrt(CHALLENGE))):
    #     for n in range(1, m):
    #         a = m**2 - n**2
    #         b = 2 * m * n
    #         c = m**2 + n**2

    #         length = a + b + c

    #         if length > CHALLENGE:
    #             break

    #         k = 1
    #         while True:
    #             if k * length > CHALLENGE:
    #                 break
    #             lengths[k * length].add((min(a * k, b * k), max(a * k, b * k), c * k))
    #             k += 1

    # res = 0
    # for elements in lengths.values():
    #     if len(elements) == 1:
    #         res += 1

    print(f"The number of unique lengths is {res}")

    return None


if __name__ == "__main__":
    main()
