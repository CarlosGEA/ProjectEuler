"""
Name : Distinct Powers
Date created : 10-07-2024
"""

LOW = 2
HIGH = 100


def main():
    nums = set()
    for a in range(LOW, HIGH + 1):
        for b in range(LOW, HIGH + 1):
            power = a**b
            nums.add(power)
    print(f"Answer is {len(nums)}")
    return None


if __name__ == "__main__":
    main()
