"""
Name : Longest Collatz Sequence
Date created : 03-06-2024
"""

MAX = 1e6


def NonRecursiveCollatz(i):
    counter = 1
    while i != 1:
        counter = counter + 1
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
    return counter


def main():

    test_nums = list(range(1, int(MAX) + 1))
    highest = 0
    max_number = 0
    for i in test_nums:
        number = i
        length = 0
        while number != 1:
            length += 1
            if (number % 2) == 0:
                number = number // 2
            else:
                number = (3 * number) + 1
        if length > highest:
            highest = length
            max_number = i
    # print(chain)
    print(f"The maximum length is size {highest}")    
    print(f"The number that produces the maximum length chain is {max_number}")

    return None


if __name__ == "__main__":
    main()
