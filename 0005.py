"""
Name : Smallest Multiple
Date created : 30-05-2024
"""
import math

TEST = 10
TEST_ANS = 2520
CHALLENGE = 20
def prime_numbers(num):
    """
    Finds all primes less than nums
    """
    primes = [1]
    for n in range(2, num + 1):
        for i in range(1, n):
            if n % i == 0 and i != 1:
                break
            if i == n - 1:
                primes.append(n)
            i += 1
    return primes

def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):         
        while n % i== 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)    
    return factors

def add_prime_factors(primes, num):
    numbers = (list(range(1,num)))
    non_primes = list(set(numbers) - set(primes))

    for n in non_primes:
        dummy_primes = [i for i in primes]
        prime_fs = primeFactors(n)
        for p in prime_fs:
            if p in dummy_primes:
                dummy_primes.remove(p)
            else:
                primes.append(p)
    return primes

def main():

    primes = prime_numbers(CHALLENGE)
    primes = add_prime_factors(primes, CHALLENGE)
    ans = math.prod(primes)
    print(
        f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {TEST} is {TEST_ANS}"
    )
    print(f"My attempt for {CHALLENGE} is {ans}")

    return None


if __name__ == "__main__":
    main()
