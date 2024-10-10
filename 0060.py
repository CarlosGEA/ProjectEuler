"""
Name : Prime Pair Sets
Date created : 21-08-2024
"""

import math, time


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
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

    start = time.time()
    primes = sieve(10000)[1:]  # if it's bigger it might find another solution

    for num in primes:
        prime_sets = [[num]]

        for b in primes:
            if b < num:
                continue
            dummy_sets = []
            for s in prime_sets:
                if all(isPrime(int(str(n) + str(b))) and isPrime(int(str(b) + str(n))) for n in s):
                    dummy_sets.append(s.copy())
                    s.append(b)

                    if len(s) == 5:
                        print(s)
                        print(f"The answer is {sum(s)}")
                        end = time.time()
                        print(f"Time: {end-start}")
                        return None
                    continue
            prime_sets += dummy_sets

    print("No solution found")

    end = time.time()
    print(f"Time: :{end-start}")
    return None


if __name__ == "__main__":
    main()
