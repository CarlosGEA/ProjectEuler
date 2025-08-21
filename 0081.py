"""
Name : Path Sum: Two Ways
Date created : 20-08-2025
"""

# do 82 and 83, 3 and 4 ways, like oranges

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0081_matrix.txt"

TRIAL = [
    ["131", "673", "234", "103", "18"],
    ["201", "96", "342", "965", "150"],
    ["630", "803", "746", "422", "111"],
    ["537", "699", "497", "121", "956"],
    ["805", "732", "524", "37", "331"],
]


def main():

    with open(FP, "r") as f:
        data = f.read()

    rows = data.split("\n")[:-1]
    matrix = []

    for r in rows:
        matrix.append(r.split(","))

    matrix = TRIAL

    nrows = len(matrix[0])
    ncols = len(matrix)

    for row in range(nrows):
        for col in range(ncols):

            if row == col == 0:
                matrix[row][col] = int(matrix[row][col])
                continue

            prev_row = float("inf") if row == 0 else int(matrix[row - 1][col])
            prev_col = float("inf") if col == 0 else int(matrix[row][col - 1])

            matrix[row][col] = int(matrix[row][col]) + min(prev_col, prev_row)

    print(matrix)

    return None


if __name__ == "__main__":
    main()
