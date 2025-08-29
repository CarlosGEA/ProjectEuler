"""
Name : Concealed Square
Date created : 22-08-2025
"""


def check(n, dig):
    str_n = str(n)
    for i in range(dig):
        if (i + 1) % 10 != int(str_n[2 * i]):
            return False
    return True


def findNextDigit(nums, digit_idx):

    if digit_idx == 8:
        return nums

    valid_nums = set()
    for start in nums:
        num = 0
        power = 10 - len(start)
        for i, dig in enumerate(start):
            num += int(dig) * 10 ** (9 - i)

        pot_num = 0
        while pot_num < 10 ** (power + 1):
            squared = (num + pot_num) ** 2
            if check(squared, digit_idx + 1) and len(str(squared)) % 2 != 0:
                valid_nums.add(
                    str(num + pot_num)[: digit_idx + 3]
                )  # maybe no need for str -> int conversion
            pot_num += 10 ** (power - 2)
    return findNextDigit(valid_nums, digit_idx + 1)


def main():

    valid_starts = {"1"}
    digit_idx = 0

    potentials = findNextDigit(valid_starts, digit_idx)
    for num in potentials:
        a = int(num) ** 2
        print(a, len(str(a)))
        if check(int(num) ** 2, 9):
            print(f"The answer is {num} with square number {int(num) ** 2}")

    return None


if __name__ == "__main__":
    main()
