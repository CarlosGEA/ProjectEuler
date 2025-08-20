"""
Name : Problem 500!!!
Date created : 19-08-2025
"""

# https://math.stackexchange.com/questions/300279/the-least-natural-number-n-which-has-18-divisors


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


"""
ans is 2^(2^4-1) * 3^(2^3-1) * 5^(2^3-1) * 7^(2^3-1) * 11^(2^2-1) * ... 193^(2^2-1) * the next 500_500 - 93 prime numbers
as there are (4 + 3 + 3 + 3 + (2 * 40)) powers of 2 used up before
Mod this all to 500500507

to make sure this doesnt exceed, keep modding as you traverse
sieve primes and iterate through

"""
MOD = 500_500_507


def main():
    primes = sieve(10_000_000)
    print(primes[396])
    print(primes[500_500-815])
    res = 1
    for n in primes[: 500_500 - 812]:  # 500,500 - (5+12+33+762)
        if n == 2:
            res *= n**31 # 2^5 (2) 5*1 = 5
        elif n <= 7:
            res *= n**15 # 2^4 (3,5,7) 4*3 = 12
        elif n <= 47:
            res *= n**7 # 2^3 (11,13,17,19,23,29,31,37,41,43,47) 3*11 = 33
        elif n <= 2713:
            res *= n**3 # 2^2 2 * (396 - 15) = 2 * 381 = 762
        else:
            res *= n # 2^1

        res = res % MOD

    res = res % MOD

    #adjust this and maybe not by hand

    print(f"The answer is {res}")
    return None


if __name__ == "__main__":
    main()
