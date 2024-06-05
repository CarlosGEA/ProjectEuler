"""
Name : Factorial Digit Sum
Date created : 05-06-2024
"""
import math

TRIAL = 10
CHALLENGE = 100

def main():
    power = int(math.factorial(CHALLENGE))
    digits_sum = sum([int(i) for i in str(power)])

    print(f"The sum of the digits of {CHALLENGE}! is {digits_sum}")
    return None



if __name__ == "__main__":
    main()