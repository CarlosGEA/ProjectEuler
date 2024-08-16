"""
Name : Lychrel Numbers
Date created : 16-08-2024
"""

N = 10_000
MAX_ITERS = 50


def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False


def main():
    count = 0
    for num in range(1, N):
        iters = 0
        new_num = num
        while iters < MAX_ITERS:
            check_num = new_num + int(str(new_num)[::-1])
            if isPalindrome(str(check_num)):
                count += 1
                break
            new_num = check_num
            iters += 1

    print(f"THe number of Lychrel numbers below {N} is {N-1-count}")
    return None


if __name__ == "__main__":
    main()
