"""
Name : Path Sum: Four Ways
Date created : 21-08-2025
"""

import heapq

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0083_matrix.txt"

TRIAL = [
    ["131", "673", "234", "103", "18"],
    ["201", "96", "342", "965", "150"],
    ["630", "803", "746", "422", "111"],
    ["537", "699", "497", "121", "956"],
    ["805", "732", "524", "37", "331"],
]


TRIAL2 = [
    ["131", "673", "434", "603", "18"],
    ["201", "96", "942", "45", "850"],
    ["630", "104", "846", "122", "111"],
    ["537", "201", "897", "61", "956"],
    ["805", "332", "24", "37", "931"],
]

# now can also go back and again from top left to bottom right
# maybe need to think about three path locally and 2 path final logic ..

def main():

    with open(FP, "r") as f:
        data = f.read()

    rows = data.split("\n")[:-1]
    matrix = []

    for r in rows:
        matrix.append(r.split(","))

    # matrix = TRIAL

    nrows = len(matrix[0])
    ncols = len(matrix)

    for row in range(nrows):
        matrix[row][0] = int(matrix[row][0])

    for col in range(1, ncols):
        queue = []
        for row in range(nrows):
            heapq.heappush(queue, (int(matrix[row][col]) + int(matrix[row][col - 1]), row))

        seen = set()
        while queue:
            number, row = heapq.heappop(queue)
            if row in seen:
                continue

            prv = row - 1
            nxt = row + 1

            if isinstance(matrix[row][col], str):
                matrix[row][col] = number

            if prv >= 0 and prv not in seen:
                heapq.heappush(queue, (int(matrix[prv][col]) + number, prv))

            if nxt < nrows and nxt not in seen:
                heapq.heappush(queue, (int(matrix[nxt][col]) + number, nxt))

            seen.add(row)

    min_last_col = float("inf")
    for row in range(nrows):
        min_last_col = min(min_last_col, matrix[row][-1])
    print(f"The shortest length path from left to right is {min_last_col}")

    return None


if __name__ == "__main__":
    main()
