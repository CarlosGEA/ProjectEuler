"""
Name : Prime Digit Replacements
Date created : 30-07-2024
"""

import itertools


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


def generate_combinations(lst):
    all_combinations = []
    for r in range(1, len(lst) + 1):
        combinations = list(itertools.combinations(lst, r))
        all_combinations.extend(combinations)
    all_combinations = [list(tup) for tup in all_combinations]
    return all_combinations


def main():

    sieve_num = 1000000
    primes = sieve(sieve_num)
    max = 0
    # print(primes, "\n", len(primes))
    for num in primes[4:]:
        replace_list = generate_combinations(range(len(str(num)) - 1))
        for replacements in replace_list:
            count = 0
            for digits in range(10):  # gives numbers 0-9
                test_str = str(num)
                for index in replacements:
                    test_str = test_str[:index] + str(digits) + test_str[index + 1 :]
                test = int(test_str)
                if test in primes and len(str(test)) == len(str(num)):
                    count += 1
            if count > max:
                max = count
                print(f"Update - new num is {num} with {max} primes")
                #######
                print_check = str(num)
                for index in replacements:
                    print_check = print_check[:index] + "*" + print_check[index + 1 :]
                print(print_check)
                #######
            if max == 7:
                print(f"Answer is {num} with {max} primes")
                return
            
    print(f"Max number of primes when sieving up to {sieve_num} is {max}")
    return None


if __name__ == "__main__":
    main()
