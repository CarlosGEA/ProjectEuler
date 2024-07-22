"""
Name : Pandigital Multiples
Date created : 15-07-2024
"""


def uniqueDigits(str_num):
    if len(str_num) == len(set(str_num)):
        return True
    return False


def main():
    max_pan = 0
    for num in range(1, 10000):
        n = 1
        str_num = ""
        while len(str_num) < 9:
            str_num += str(num * n)
            n += 1
        if '0' not in str_num and uniqueDigits(str_num) and n > 1 and int(str_num) > max_pan:
            max_pan = int(str_num)

    print(max_pan)
    return None


if __name__ == "__main__":
    main()
