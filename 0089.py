"""
Name : Roman Numerals
Date created : 29-08-2025
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0089_roman.txt"

# VIIII -> VIV -> IX as can't have 2 V's
# iterate backwards for each number, reducing

TRIAL = ["XXXXVIIII"]


def main():

    NUMERAL_ID = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
    # NEXT_NUMERAL = {"I": "V", "V": "X", "X": "L", "L": "C", "C": "D", "D": "M"}

    with open(FP, "r") as f:
        data = f.read()

    numerals = data.split("\n")

    total_count = 0

    for numeral in numerals:
    # for numeral in TRIAL:
        letter_count = [0] * 7
        initial_size = len(numeral)
        for letter in numeral:
            letter_count[NUMERAL_ID[letter]] += 1

        final_size = 0
        for id in range(7):
            if id != 6 and letter_count[id] == 5:
                letter_count[id] = 0
                letter_count[id + 1] += 1

            elif id != 6 and letter_count[id] == 4:
                letter_count[id] = 1
                letter_count[id + 1] += 1

            elif letter_count[id] > 1 and id % 2 != 0:
                letter_count[id] = 0
                letter_count[id + 1] += 1

            final_size += letter_count[id]

        total_count += initial_size - final_size

        # count_saved = 0
        # cur = None
        # cur_count = 0

    #     for letter in numeral[::-1]:

    #         if letter != cur:
    #             cur = letter
    #             cur_count = 1

    #         else:
    #             cur_count += 1

    #         # account for fact it can reach 5 and count_saved is += 4
    #         if cur_count == 4 and cur != "M":
    #             count_saved += 2
    #             cur = NEXT_NUMERAL[cur]
    #             cur_count = 1

    #         elif cur in "VLD" and cur_count > 1:
    #             count_saved += 1
    #             cur = NEXT_NUMERAL[cur]
    #             cur_count = 1

    #     print(numeral, count_saved)
    #     total_count += count_saved
    print(total_count)

    # still wrong

    return None


if __name__ == "__main__":
    main()
