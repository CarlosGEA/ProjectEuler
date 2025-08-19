"""
Name : Bouncy Numbers
Date created : 19-08-2025
"""


def isBouncy(n):
    str_n = str(n)

    if len(str_n) < 3:
        return False

    n1 = int(str_n[0])
    n2 = int(str_n[-1])

    increasing = n1 < n2

    for num_str in str_n[1:-1]:
        num = int(num_str)
        if increasing:
            if not n1 <= num <= n2:
                return True
            n1 = max(n1, num)

        else:
            if not n1 >= num >= n2:
                return True
            n1 = min(n1, num)

    return False


def main():

    bouncy = 0
    for i in range(1, 10000000):
        if isBouncy(i):
            bouncy += 1

        if bouncy / i >= 0.99:
            print(f"The point at which the proportion of bouncy numbers is 0.99 is at {i}")
            break

    print(f"Final proportion of bouncy numbers : {bouncy / i} and amount {bouncy}")


    return None


if __name__ == "__main__":
    main()
