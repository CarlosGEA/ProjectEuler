"""
Name : Distinct Primes Factors
Date created : 27-07-2024
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


def factorise_n(num):
    i = 2
    factors = set()
    while i <= num:
        while num % i == 0:
            factors.add(i)
            num = num / i
        if i == 2:
            i += 1
        else:
            i += 2
    return factors


def main():
    dpf = []
    n = 647
    while len(dpf) != 4:
        n += 1
        if isPrime(n):
            dpf = []
            continue
        elif len(factorise_n(n)) == 4:
            dpf.append(n)
        else:
            dpf = []
    print(dpf)
    print(f"The first 4 consecutive integers with 4 distinct prime factors is {dpf[0]}")

    return None

""" Online solution using sieve, basically instantaneous answer """
# def main():

#     target = 4  # number of prime factors and successive integers
#     limit = 150000  # arbitrary upper-bound on the search, found by trial and error
#     n_prime_divisors = [0] * limit  # the number of prime divisors of each integer considered

#     run_length = 0  # length of the current run of valid integers
#     for n in range(2, limit):
#         if n_prime_divisors[n] == 0:
#             # n is prime, sieve out multiples of n
#             for m in range(2 * n, limit, n):
#                 n_prime_divisors[m] += 1  # m is divisible by n (prime)
#             run_length = 0  # n is invalid, reset our run counter
#         elif n_prime_divisors[n] == target:
#             run_length += 1  # n is valid, increment our run counter
#         else:
#             run_length = 0  # n is invalid, reset our run counter

#         if run_length == target:
#             break

#     print(f"Answer is {n - target + 1}")
#     return None


if __name__ == "__main__":
    main()
