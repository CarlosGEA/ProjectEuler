"""
Name : Permuted Multiples
Date created : 14-08-2024
"""


def isPermutation(num, compare):
    return sorted(str(num)) == sorted(str(compare))


def main():

    mults = [3, 4, 5, 6]
    i = 1
    while True:
        num = 2 * i
        for multiple in mults:
            test = i * multiple
            if not isPermutation(num, test):
                break
        else:
            print(f"The answer is {i}")
            return
        i += 1


if __name__ == "__main__":
    main()
