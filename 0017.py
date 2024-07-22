"""
Name : Number Letter Counts
Date created : 04-06-2024
"""

NUM_OF_LETTERS_KEY = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8,
}

TRIAL = 505
CHALLENGE = 1000


def num_to_num_of_letters(num):  # use memoization for 1-9
    num_letters = 0
    while num != 0:
        if num <= 20:
            num_letters += NUM_OF_LETTERS_KEY[num]
            num = 0
        elif num < 100:
            num_letters += NUM_OF_LETTERS_KEY[num - num % 10]
            num = num % 10
        elif num < 1000:
            num_letters += NUM_OF_LETTERS_KEY[100] + NUM_OF_LETTERS_KEY[num // 100]
            if num % 100 != 0:
                num_letters += 3
            num = num % 100
        else:
            num_letters += NUM_OF_LETTERS_KEY[num] + NUM_OF_LETTERS_KEY[num // 1000]
            num = 0

    return num_letters


def main():
    count = 0
    for i in range(1, CHALLENGE + 1):
        count += num_to_num_of_letters(i)

    print(
        f"If all the numbers from 1 to {CHALLENGE} were written out in words, {count} letters would be used."
    )
    return None


if __name__ == "__main__":
    main()
