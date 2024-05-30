"""
Name : 10001st Prime
Date created : 30/05/2024
"""

TEST = 6
CHALLENGE = 10001


def prime(nth):
    primes = [2]
    i = 2
    while len(primes) < nth:
        for num in range(2, i):
            if i % num == 0:
                break
            elif num == i - 1 and i not in primes:
                primes.append(i)
        i += 1
    return primes


def main():

    # sol = prime(TEST)
    primes = prime(CHALLENGE)
    sol = primes[-1]
    print(f"Prime number {TEST} is 13.")
    print(f"My prime number {CHALLENGE} is {sol}.")

    return None


if __name__ == "__main__":
    main()
