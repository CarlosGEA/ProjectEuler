"""
Name : Champernowne's Constant
Date created : 19-07-2024
"""


def main():

    frac_string = ""
    num = 1
    while len(frac_string) < 1_000_000:
        frac_string += str(num)
        num += 1

    prod = 1
    for i in range(0, 7):
        prod *= int(frac_string[10**i - 1])

    print(prod)
    return None


if __name__ == "__main__":
    main()
