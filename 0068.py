"""
Name : Magic 5-gon Ring
Date created : 05-08-2025
"""

TRIAL = range(1,7)
CHALLENGE = range(1,11)

def main():
    """
    Figured out that for an n gon you have n / 2 repeat digits
    These can be either the first n, second n or n either odd/even n
    E.g. 1,2,3,4,5,6 - Repeat either {1,2,3} or {4,5,6} or {1,3,5} or {2,4,6}
    For a 5 gon with digits up to 10, if the 10 repeats you will have 17 digits and 16 otherwise 
    thus for a 16 digit number you want 10 to not repeat so either {1,2,3,4,5} or {1,3,5,7,9}
    You start the numbers with the smallest outer digits i.e. the non repeating ones so either 6 from {6,7,8,9,10} or 2 from {2,4,6,8,10}
    Therefore you want to repeat {1,2,3,4,5}. This gives an average of 6 to pair with an average of 8 for a total of 14 in each line.
    So pair the 6 with 5 and 3, and 10 with 3 and 1. Then the 7 with 5 and 2, and 9 with 4 and 1. 8 goes with 2 and 4.
    Largest is then 653 as 653 > 635 and what follows is 1031, 914, 842,725
    """
   

    return None


if __name__ == "__main__":
    main()