"""
Name : Powerful Digit Sum
Date created : 16-08-2024
"""


def main():
    max = 0
    for a in range(0, 100):
        for b in range(0, 100):
            d_sum = sum(map(int, list(str(a**b))))
            if d_sum > max:
                max = d_sum
    print(f"The maximum digital sum is {max}")

    return None


if __name__ == "__main__":
    main()
