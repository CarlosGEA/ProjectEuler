"""
Name : Double-base Palindromes
Date created : 14-07-2024
"""

import time

MAX = 1_000_000


def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False


start_time = time.time()


def main():

    palindrome_nums = []
    for num in range(1, MAX + 1):
        str_num = str(num)
        str_bin = bin(num)[2:]
        if isPalindrome(str_num) and isPalindrome(str_bin):
            palindrome_nums.append(num)
    print(f"The sum of all Double-base palindromes less than {MAX} is {sum(palindrome_nums)}")

    return None


if __name__ == "__main__":
    main()
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
