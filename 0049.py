"""
Name : Prime Permutations
Date created : 28-07-2024
"""

import math


def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(6, math.floor(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % (x + 1) == 0:
            return False
    return True


def isPermutation(num, compare):
    return sorted(str(num)) == sorted(str(compare))


def main():

    n = 1001
    ans = ""
    while len(ans) < 12:
        dummy = n
        diff = 2
        ans = str(n)
        while dummy < 10_000:
            dummy += diff
            if not isPrime(n) or dummy > 10000:
                n += 2
                ans = ""
                dummy = n
                break
            elif not isPermutation(dummy, n) or not isPrime(dummy):
                diff += 2
                dummy = n
                ans = str(n)
            else:
                ans += str(dummy)
            if len(ans) == 12 and n != 1487:
                break

    print(n, dummy, diff)
    print(ans)

    return None


if __name__ == "__main__":
    main()
