"""
Name : Names Scores
Date created : 05-06-2024
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\names.txt"


def main():

    with open(FP, "r") as f:
        names = f.read()
    names = [x.strip('"') for x in names.split(",")]
    names.sort()
    print(len(names))
    total = 0
    for idx, name in enumerate(names):
        name_sum = sum([ord(i) - 64 for i in name])  # if using lowercase "-96"
        total += name_sum * (idx + 1)
    print(f"The answer is {total}")

    return None


if __name__ == "__main__":
    main()
