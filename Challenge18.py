"""
Name : Maximum Path Sum I
Date created : 04-06-2024
"""

CHALLENGE = (
    "75 "
    "95 64 "
    "17 47 82 "
    "18 35 87 10 "
    "20 04 82 47 65 "
    "19 01 23 75 03 34 "
    "88 02 77 73 07 63 67 "
    "99 65 04 28 06 16 70 92 "
    "41 41 26 56 83 40 80 70 33 "
    "41 48 72 33 47 32 37 16 94 29 "
    "53 71 44 65 25 43 91 52 97 51 14 "
    "70 11 33 28 77 73 17 78 39 68 17 57 "
    "91 71 52 38 17 14 91 43 58 50 27 29 48 "
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31 "
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 "
)

TRIAL = "3 " "7 4 " "2 4 6 " "8 5 9 3 "

# do running highest count for each number down the grid


def setup(input, rows):
    triangle = input.split(" ")
    grid = []
    count = 0
    for i in range(1, rows + 1):
        grid.append([int(x) for x in triangle[count : count + i]])
        count += i
    return grid


def search(row, grid, position_count=None):

    if position_count == None:
        position_count = {}

    if row == 0:
        position_count[(0, 0)] = grid[0][0]
        return position_count
    else:
        position_count = search(row - 1, grid, position_count)
        for elem in range(row + 1):
            if elem == 0:
                prev_count = position_count[(row - 1, elem)]
            elif elem == row:
                prev_count = position_count[(row - 1, elem - 1)]
            else:
                prev_count = max(
                    position_count[(row - 1, elem - 1)], position_count[(row - 1, elem)]
                )
            count = prev_count + grid[row][elem]
            position_count[(row, elem)] = count
        return position_count


def main():
    rows = 15
    grid = setup(CHALLENGE, rows)
    position_counts = search(rows - 1, grid)
    max_count = 0
    for elem in range(rows):
        max_count = max(max_count, position_counts[(rows - 1, elem)])
    print(f"The maximum sum path is {max_count}")
    return None


if __name__ == "__main__":
    main()
