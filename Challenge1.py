"""
Name : Multiples of 3 or 5 
Date created : 27-05-2024
"""

N = 1000


def Me(n):

    total_sum = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            total_sum += i
    return total_sum

def main():
    
    ans = Me(N)
    print(f"Sum of all the multiples of 3 or 5 below {N} : {ans}")
    
    return None


if __name__ == "__main__":
    main()





