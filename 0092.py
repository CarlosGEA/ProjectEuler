"""
Name : Square Digit Chains
Date created : 21-08-2025
"""

import time

TRIAL = 3
CHALLENGE = 10_000_000
MEMO = {}


def chainCalc(num):
    res = 0
    for dig in str(num):
        res += int(dig) ** 2

    return res


def main():

    res = 0

    seen89 = {89}
    seen1 = {1}

    for num in range(1, CHALLENGE):
        cur = num
        count = 0
        cur_seen = set()
        while cur not in seen89 and cur not in seen1:
            cur_seen.add(cur)
            if cur < CHALLENGE:
                count += 1
            cur = chainCalc(cur)

        if cur in seen89:
            res += count
            seen89.update(cur_seen)

        else:
            seen1.update(cur_seen)

    print(f"The number of numbers that go to 89 is {res + 1 if CHALLENGE >= 89 else res}")
    return None


# 3, 9, 81, 65, 61, 37, 58,89

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
