"""
Name : Triangle Words
Date created : 20-07-2024
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0042_words.txt"


def generateTriangleNumbers(n):
    return int(n * (n + 1) / 2)


def main():

    with open(FP, "r") as f:
        data = f.read()
    words = [x.strip('"') for x in data.split(",")]

    triangle_numbers = [1]
    n = 1
    triangle_words = 0
    for word in words:
        word_sum = sum([ord(i) - 64 for i in word])
        while word_sum > max(triangle_numbers):
            n += 1
            triangle_numbers.append(generateTriangleNumbers(n))
        if word_sum in triangle_numbers:
            triangle_words += 1

    print(f"There are {triangle_words} triangle words in this file")
    return None


if __name__ == "__main__":
    main()
