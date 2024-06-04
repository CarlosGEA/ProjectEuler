"""
Name : Lattice Paths
Date created : 03-06-2024
"""

import math

TRIAL = 2
CHALLENGE = 20


def main():

    combinations = math.factorial(CHALLENGE * 2)
    repeats = math.factorial(CHALLENGE) * math.factorial(CHALLENGE)
    ans = combinations / repeats
    print(f"The number of paths for a lattice of size {CHALLENGE}x{CHALLENGE} is {int(ans)}")

    

    return None


if __name__ == "__main__":
    main()

# Good recursion method
# from typing import Dict, List, Optional, Tuple


# def search(
#     length: int,
#     moves: Optional[List[int]] = None,
#     solutions: Optional[Dict[Tuple[int, int], int]] = None,
# ) -> int:
#     """Recursive tree search, branching on possible choices (left or down)

#     Dynamic programming (solutions) is used to cache previous, partial, answers avoiding re-computation.

#     :param length: the length of each axis in the grid
#     :param moves: the moves made (down and right) at this point of the search
#     :param solutions: partial solutions cache for the avoidance of redundant computations
#     :return: the number of search paths through a :math:`length \\times length` grid
#     """

#     if moves is None:
#         moves = [0, 0]  # initialise moves to represent none have been made

#     assert moves[0] <= length, "you cannot move past the edge"
#     assert moves[1] <= length, "you cannot move past the edge"

#     if solutions is None:
#         solutions = {}  # initialise solutions to the empty cache

#     if moves[0] == length:
#         return 1  # base case: no further branching possible
#     elif moves[1] == length:
#         return 1  # base case: no further branching possible
#     elif tuple(moves) in solutions:
#         return solutions[tuple(moves)]  # returned cached answer
#     else:
#         # Branch down each possible path via recursion
#         answer0 = search(length, [moves[0] + 1, moves[1]], solutions)
#         print("A0: ", [moves[0] + 1, moves[1]], answer0)
#         solutions[(moves[0] + 1, moves[1])] = answer0
#         answer1 = search(length, [moves[0], moves[1] + 1], solutions)
#         print("A1: ", [moves[0], moves[1] + 1], answer1)
#         solutions[(moves[0], moves[1] + 1)] = answer1
#         return answer0 + answer1


# def solve():
#     """Compute the answer to Project Euler's problem #15"""
#     target = 3
#     answer = search(target)
#     return answer


# ans = solve()
# print(ans)


