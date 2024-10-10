"""
Name : Lattice Paths
Date created : 03-06-2024
"""

import math

TRIAL = 2
CHALLENGE = 20


def main():

    combinations = math.factorial(CHALLENGE * 2)
    repeats = math.factorial(CHALLENGE) * math.factorial(CHALLENGE)
    ans = combinations / repeats
    print(f"The number of paths for a lattice of size {CHALLENGE}x{CHALLENGE} is {int(ans)}")

    return None


if __name__ == "__main__":
    main()

# Good recursion method in previous version