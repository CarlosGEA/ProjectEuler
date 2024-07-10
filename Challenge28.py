"""
Name : Number Spiral Diagonals
Date created : 10-07-2024
"""

TRIAL = 5
CHALLENGE = 1001


def main():
    iters = (CHALLENGE - 1) // 2
    count = 1
    high = 1
    for i in range(iters):
        diff = 2 * (i + 1)
        low = high + diff
        high = low + (diff * 3)
        # print(low, high)
        count += 2 * (low + high)

    print(f"The sum of all diagonal elements in a {CHALLENGE}x{CHALLENGE} square is {count}")
    return None


if __name__ == "__main__":
    main()
