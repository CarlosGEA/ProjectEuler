"""
Name : Large Non-Mersenne Prime
Date created : 05-08-2025
"""

def main():

    """
    Find the last 10 digits of 28433 *  2 ^ 7830457 + 1
    """

    n = 7830457
    num = 1
    for _ in range(n):
        num *= 2

        num_str = str(num)
        num_str = num_str[-10:]
        num = int(num_str)

    num *= 28433
    num += 1
    num_str = str(num)
    num_str = num_str[-10:]
    num = int(num_str)

    print(f"The last ten digits of this large non-Mersenne prime number is {num}")

    return None


if __name__ == "__main__":
    main()