"""
Name : Sum of even Fibonnaci numbers less than 4e6 
Date created : 27-05-2024
"""

MAX = 4e6

def fib(n0, n1):
    sequence = [n0, n1]
    while (n2 := n0 + n1) < MAX:
        n0 = n1
        n1 = n2
        sequence.append(n2)
    return sequence

def even(sequence):
    evens = []
    for i in sequence:
        if (i % 2) == 0:
            evens.append(i)
    return evens


def main():
    n0 = 1  
    n1 = 2
    sequence = fib(n0, n1)
    print(f" Sequence of fibonacci numbers starting with {n0} and {n1} and less than {MAX:.0e}: \n {sequence}")
    even_sequence = even(sequence)
    print(f" Even sequence of fibonacci numbers starting with {n0} and {n1} and less than {MAX:.0e}: \n {even_sequence}")
    print(f"Sum of even numbers in above list is : {sum(even_sequence)}")
    
    return None


if __name__ == "__main__":
    main()





