"""
Name : 1000-digit Fibonnaci Number
Date created : 03-07-2024
"""

TRIAL = 3
CHALLENGE = 1000

def main():
    n0 = 0
    n1 = 1
    count = 1
    while len(str(n1)) < CHALLENGE:
        temp = n1
        n1 += n0
        n0 = temp
        count += 1
    print(f"The smallest {CHALLENGE} digit number in the fibonacci sequence is index {count}")
   
    return None


if __name__ == "__main__":
    main()