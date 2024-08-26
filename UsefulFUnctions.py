import math

def getFactors(n):
    """
    Gets factors not including 1 and itself, if you want them make factor_list = [1, n]
    """
    factor_list = []
    val = math.ceil(math.sqrt(n))
    for i in range(2, val):
        if n % i == 0:
            factor_list.extend([i, n // i])
    if val**2 == n and n != 1:
        factor_list.append(val)
    return factor_list


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

def isPandigital(str_num):
    if len(str_num) == len(set(str_num)):
        return True
    return False

def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


# [ord(i) - 64 for i in word] - word to digits

def isTriangular(num):
    return math.isqrt(1 + 8 * num) and ((-1 + math.sqrt(1 + 8 * num)) % 2 == 0)


def isSquare(num):
    return math.isqrt(num)


def isPentagonal(num):
    return math.isqrt(1 + 24 * num) and ((1 + math.sqrt(1 + 24 * num)) % 6 == 0)


def isHexagonal(num):
    return math.isqrt(1 + 8 * num) and ((1 + math.sqrt(1 + 8 * num)) % 4 == 0)


def isHeptagonal(num):
    return math.isqrt(9 + 40 * num) and ((3 + math.sqrt(9 + 40 * num)) % 10 == 0)


def isOctogonal(num):
    return math.isqrt(1 + 3 * num) and ((1 + math.sqrt(1 + 3 * num)) % 3 == 0)


def isCylic(nums):
    for idx, n in enumerate(nums):
        if not str(n)[2:] == str(nums[(idx + 1) % len(nums)])[:2]:
            return False
    return True
