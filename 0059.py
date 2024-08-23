"""
Name : XOR Decryption
Date created : 16-08-2024
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0059_cipher.txt"

KEY = range(97, 123)  # ASCII characters a-z
COMMON_WORDS = ["the", "from", "to", "is", "and", "from", "it", "for"]
COMMON_CHARS = list(range(32, 127))


def main():

    with open(FP, "r") as f:
        data = f.read()
    numbers = [int(i) for i in data.split(",")]

    for l1 in KEY:
        for l2 in KEY:
            for l3 in KEY:
                decoded_lets = []
                key = [l1, l2, l3]

                for idx, num in enumerate(numbers):
                    decoded_num = num ^ int(key[idx % 3])
                    decoded_lets.append(chr(decoded_num))
                    if decoded_num not in COMMON_CHARS:
                        break
                else:
                    decoded_phrase = "".join(decoded_lets)
                    if all(substring in decoded_phrase for substring in COMMON_WORDS):
                        print(f"Key: {key}")
                        print(decoded_phrase)
                        print(sum([ord(l) for l in decoded_lets]))
                        return
                    continue
    print("No solution found :(")
    return None


if __name__ == "__main__":
    main()
