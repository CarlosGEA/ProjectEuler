"""
Name : Prime Pair Sets
Date created : 21-08-2024
"""

import math

def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


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


def main():

    primes = sieve(10000)[1:]
    prime_sets = []

    for num in primes:
        print(num)
        if num < 1000:
            prime_sets.append([num])
        dummy_sets = []
        for s in prime_sets:
            if all(isPrime(int(str(n) + str(num))) and isPrime(int(str(num) + str(n))) for n in s):
                dummy_sets.append(s.copy())
                s.append(num)
                continue
        prime_sets += dummy_sets
    min_sum = 0
    for p in prime_sets:
        if len(p) == 5:
            print(p)
            if min_sum == 0:
                min_sum = sum(p)
            elif sum(p) < min_sum:
                min_sum = sum(p)
    if min_sum != 0:
        print(f"The answer is {min_sum}")
    else:
        print("No solution found")
    return None


# make more efficient


if __name__ == "__main__":
    main()
