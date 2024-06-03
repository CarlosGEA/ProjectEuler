"""
Name : 
Date created : 03-06-2024
"""

MAX = 1e6


def main():

    chain = []
    for i in range(2, int(MAX)+1):
        print(i)
        number = i
        if number in chain:
            continue
        while number != 1:
            if number in chain:
                break
            else:
                chain.append(number)

            if (number % 2) == 0:
                number = number // 2
            else:
                number = (3 * number) + 1
        chain.append(number)

    # print(chain)
    print(f"The maximum length is size {len(chain)}")

    return None


if __name__ == "__main__":
    main()
