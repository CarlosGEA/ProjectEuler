"""
Name : Power Digit Sum
Date created : 03-06-2024
"""

import math

TRIAL = 15
CHALLENGE = 1000

def main():
    power = int(math.pow(2, CHALLENGE))
    digits_sum = sum([int(i) for i in str(power)])

    print(f"The sum of the digits of 2^{CHALLENGE} is {digits_sum}")
    return None


if __name__ == "__main__":
    main()