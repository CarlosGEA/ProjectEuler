"""
Name : Convergence of e
Date created : 09-03-2025
"""


def calcTruncatedFraction(start, a_terms):
    # [ ... , a, b ] = [ ... , a + 1/b ]

    numer = 0
    denom = 1

    for a in a_terms:
        numer += a * denom
        numer, denom = denom, numer
    numer += start * denom

    return numer, denom


def main():
    euler_continued_fraction = [2, 1, 2]
    i = 2
    while len(euler_continued_fraction) < 100:
        euler_continued_fraction += [1, 1, i * 2]
        i += 1

    start = euler_continued_fraction[0]
    a_terms = euler_continued_fraction[1:100][::-1]
    # a_terms = euler_continued_fraction[1:10][::-1]

    numerator, denominator = calcTruncatedFraction(start, a_terms)
    numerator_str = str(numerator)
    res = 0
    for n in numerator_str:
        res += int(n)

    print(
        f"The sum of digits in the numerator of the 100th convergent of the continued fraction for e is {res}."
    )

    return None


if __name__ == "__main__":
    main()
