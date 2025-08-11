"""
Name : Totient Maximum
Date created : 10-08-2025
"""

TRIAL = 10
CHALLENGE = 1_000_000


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


def main():
    # Only check even numbers as odds will have ratio of x / y where y >= 0.5x and thus ratio <= 2 which we know is not the greatest
    # Can extend this through intuition and looking at the maths
    # Conclusion is that the ratio increases with each new prime factor, so use all smallest prime factors that multiply and give less than 10^6

    result = 1
    primes = sieve(100)
    for prime in primes:
        if result * prime > CHALLENGE:
            print(f"The answer is {result}")
            return 
        result *= prime

    return None


if __name__ == "__main__":
    main()
