"""
Name : Digit Cancelling Fractions
Date created : 12-07-2024
"""

import math


def main():

    non_trivial_fractions = []
    for numerator in range(11, 100):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 or denominator % 10 == 0:
                continue

            str_n = str(numerator)
            str_d = str(denominator)
            common = set(str_n).intersection(set(str_d))
            if common:
                c_numerator = int(str_n.replace(list(common)[0], "", 1))
                c_denominator = int(str_d.replace(list(common)[0], "", 1))

                normal_frac = numerator / denominator
                cancel_frac = c_numerator / c_denominator

            if normal_frac == cancel_frac and int(cancel_frac) != 1:
                non_trivial_fractions.append(normal_frac)

    overall_denominator = int(math.prod([1 / x for x in non_trivial_fractions]))

    print(non_trivial_fractions)
    print(overall_denominator)
    return None


if __name__ == "__main__":
    main()
