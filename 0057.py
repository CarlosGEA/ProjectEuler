"""
Name : Square Root Convergents
Date created : 16-08-2024
"""

MAX_ITER = 1000


def main():
    num_0, denom_0 = 3, 2
    num_1, denom_1 = 7, 5

    count = 0
    for _ in range(1, MAX_ITER):
        num_1, num_0 = 2 * num_1 + num_0, num_1
        denom_1, denom_0 = 2 * denom_1 + denom_0, denom_1
        if len(str(num_1)) > len(str(denom_1)):
            count += 1

    print(f"The answer is {count}")
    return None


if __name__ == "__main__":
    main()
