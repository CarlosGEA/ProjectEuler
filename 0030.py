"""
Name : Digit Fifth Powers
Date created : 10-07-2024
"""

TRIAL = 4
CHALLENGE = 5


def main():

    digits = []
    # upper bound found from # of numbers in x * 9^5 < x (x = 7) here
    for num in range(2, 413343): 
        num_list = [i for i in str(num)]
        count = 0
        for elem in num_list:
            count += int(elem) ** CHALLENGE
        if count == num:
            digits.append(num)
    print(digits)
    print(
        f"Sum of numbers that can be written as sum of {CHALLENGE}th powers of their digits is {sum(digits)}"
    )
    return None


if __name__ == "__main__":
    main()
