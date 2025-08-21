"""
Name : Prime Power Triples
Date created : 21-08-2025
"""

import time


TRIAL = 50
CHALLENGE = 50_000_000


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


def getPowers(i, primes):
    nums_to_power = []
    for p in primes:
        num = p**i
        nums_to_power.append(num)
        if num > CHALLENGE:
            break

    return nums_to_power


def main():

    primes = sieve(7100)

    squares = getPowers(2, primes)
    cubes = getPowers(3, primes)
    fourths = getPowers(4, primes)

    res = 0

    seen = set()
    for n4 in fourths:
        for n3 in cubes:
            for n2 in squares:
                powers_sum = n2 + n3 + n4
                # if powers_sum < TRIAL and powers_sum not in seen:
                if powers_sum < CHALLENGE and powers_sum not in seen:
                    seen.add(powers_sum)
                    res += 1

    print(res)

    return None


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
