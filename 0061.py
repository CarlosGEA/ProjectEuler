"""
Name : Cyclical Figurate Numbers
Date created : 23-08-2024
"""

import copy


def isCylic(nums):
    for idx, n in enumerate(nums):
        if not str(n)[2:] == str(nums[(idx + 1) % len(nums)])[:2]:
            return False
    return True


def generateTriangle(n):
    return int(n * (n + 1) / 2)


def generateSquare(n):
    return int(n * n)


def generatePentagonal(n):
    return int(n * (3 * n - 1) / 2)


def generateHexagonal(n):
    return int(n * (2 * n - 1))


def generateHeptagonal(n):
    return int(n * (5 * n - 3) / 2)


def generateOctagonal(n):
    return int(n * (3 * n - 2))


def getValidPolygonals():
    tns, sns, pns, xns, hns, ons = [1], [1], [1], [1], [1], [1]
    n = 2

    while True:
        if ons[-1] < 10_000:
            ons.append(generateOctagonal(n))
        if hns[-1] < 10_000:
            hns.append(generateHeptagonal(n))
        if xns[-1] < 10_000:
            xns.append(generateHexagonal(n))
        if pns[-1] < 10_000:
            pns.append(generatePentagonal(n))
        if sns[-1] < 10_000:
            sns.append(generateSquare(n))
        if tns[-1] < 10_000:
            tns.append(generateTriangle(n))
        else:
            break
        n += 1
    ons = [n for n in ons[:-1] if n > 1000 and str(n)[-2] != "0"]
    hns = [n for n in hns[:-1] if n > 1000 and str(n)[-2] != "0"]
    xns = [n for n in xns[:-1] if n > 1000 and str(n)[-2] != "0"]
    pns = [n for n in pns[:-1] if n > 1000 and str(n)[-2] != "0"]
    sns = [n for n in sns[:-1] if n > 1000 and str(n)[-2] != "0"]
    tns = [n for n in tns[:-1] if n > 1000 and str(n)[-2] != "0"]

    return {
        "Triangle": tns,
        "Square": sns,
        "Pentagonal": pns,
        "Hexagonal": xns,
        "Heptagonal": hns,
        "Octagonal": ons,
    }


def sol(nums, search_dict, count=[1]):

    if len(nums) == 6:  # 3
        # print(f"Potential solution : {nums}")
        if str(nums[-1])[2:] == str(nums[0])[:2]:
            print(f"The answer is {sum(nums)} with numbers {nums} and count {count[0]}")
            return True
        else:
            nums.pop()
            count[0] -= 1
            return False

    # print(f"Nums: {nums} | Count: {count} | Where to search: {search_dict.keys()}")
    repeat = str(nums[count[0] - 1])[2:]
    for k in search_dict.keys():
        for n in search_dict[k]:
            if str(n)[:2] == repeat:
                dummy_dict = copy.deepcopy(search_dict)
                del dummy_dict[k]
                nums.append(n)
                count[0] += 1
                if sol(nums, dummy_dict, count):
                    return True

    if count[0] > 1:
        # print(f"No direct sol", nums, count, search_dict.keys())
        nums.pop()
        count[0] -= 1
    return False


def main():

    polygonal_dict = getValidPolygonals()
    keys = list(polygonal_dict.keys())[::-1]

    start = keys[0]

    dummy_dict = dict(polygonal_dict)
    del dummy_dict[start]
    for num in polygonal_dict[start]:

        if sol([num], dummy_dict):
            break

    return None


if __name__ == "__main__":
    main()
