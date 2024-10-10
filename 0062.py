"""
Name : Cubic Permutations
Date created : 25-08-2024
"""

from collections import defaultdict

def genCubes():
    cubes_dict = defaultdict(list)

    for i in range(1, 10_000):
        c = i**3
        clen = len(str(c))
        cubes_dict[clen].append(c)

    return cubes_dict


def isPermutation(num, compare):
    return sorted(str(num)) == sorted(str(compare))


def main():

    cubes = genCubes()

    for slc in list(cubes.values()):
        for c in slc:
            nums = [x for x in slc if isPermutation(x, c)]
            if len(nums) == 5:
                print(f"The answer is {c} with {nums}")
                return
    print("No solution yet")
    return None

## Super quick solution found online
# cubes = []
# i = 0

# while True:
#     cube = sorted(list(str(i**3)))
#     cubes.append(cube)
#     if cubes.count(cube) == 5:
#         print(cubes.index(cube)**3)
#         break
#     i += 1


if __name__ == "__main__":
    main()