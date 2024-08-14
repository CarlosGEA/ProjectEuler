"""
Name : Self Powers
Date created : 27-07-2024
"""


def main():
    ans = 0
    for i in range(1, 1001):
        ans += i**i
    print(f"The answer is {str(ans)[-10:]}")

    return None


if __name__ == "__main__":
    main()
