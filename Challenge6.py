"""
Name : Sum Square Difference
Date created : 30/05/2024
"""

TEST = 10
CHALLENGE = 100


def calc(n):

    result = 0
    for i in range(n, 1, -1):
        for j in range(i-1, 0, -1):
           result += (2*i*j)
    return result

def main():
   
    result = calc(CHALLENGE)
    print(f"The difference between sum of square and square of sums up to 10 is 3025-385=2640\n")
    print(f"My difference between sum of square and square of sums up to {CHALLENGE} is {result}\n")
    return None


if __name__ == "__main__":
    main()