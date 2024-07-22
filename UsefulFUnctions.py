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

# [ord(i) - 64 for i in word] - word to digits

