"""
Name : Largest Prime Factor 
Date created : 28-05-2024
"""
NUMBER = 600851475143
TRIAL  = 13195
MAX_TRIAL = 29

def factorise_n(num):
    i = 1
    factors = []
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num = num / i
        i += 1
    return factors

def main():

    factors = factorise_n(NUMBER)
    print(f" The factors of {NUMBER} are {factors}")
    print(f" The largest prime factor of {NUMBER} is {factors[-1]}")
    return None


if __name__ == "__main__":
    main()




