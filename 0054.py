"""
Name : Poker Hands
Date created : 15-08-2024
"""

from collections import Counter


FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0054_poker.txt"

RANK = {"HC": 0, "OP": 1, "TP": 2, "TOK": 3, "S": 4, "F": 5, "FH": 6, "FOK": 7, "SF": 8, "RF": 9}


def checkStraight(nums):
    return nums == list(range(min(nums), max(nums) + 1))

def valueToNums(nums):
    for idx, num in enumerate(nums):
        if num == "T":
            nums[idx] = "10"
        elif num == "J":
            nums[idx] = "11"
        elif num == "Q":
            nums[idx] = "12"
        elif num == "K":
            nums[idx] = "13"
        elif num == "A" and "".join(sorted(nums)) == "2345A":
            nums[idx] = "1"
        elif num == "A":
            nums[idx] = "14"
    sorted_nums = sorted([int(i) for i in nums])
    return sorted_nums

def checkHands(cards):
    cards = cards.split(" ")[:5]
    value, suits = map(list, zip(*[(i[0], i[1]) for i in cards]))
    nums = valueToNums(value)

    # Check Flushes
    if len(set(suits)) == 1:
        if checkStraight(nums):
            if nums[-1] == 14:
                return ["RF"]
            else:
                return ["SF", nums[-1]]
        return ["F"] + nums[::-1]
    # Check Straights
    if checkStraight(nums):
        return ["S"] + nums[::-1]

    # Check x of a Kind
    kinds = dict(Counter(nums).most_common())
    order = list(kinds.keys())
    if 4 in kinds.values():
        return ["FOK"] + order
    elif 3 in kinds.values() and 2 in kinds.values():
        return ["FH"] + order
    elif 3 in kinds.values():
        order[1:] = sorted(order[1:])[::-1]
        return ["TOK"] + order
    num_pairs = sum(x == 2 for x in kinds.values())
    if num_pairs == 2:
        order[:2] = sorted(order[:2])[::-1]
        return ["TP"] + order
    elif num_pairs == 1:
        order[1:] = sorted(order[1:])[::-1]
        return ["OP"] + order
    else:
        order = sorted(order)[::-1]
        return ["HC"] + order


def main():
    with open(FP, "r") as f:
        data = f.read()
    games = 1000
    p1_wins = 0
    for game in range(games):

        p1_scores = checkHands(data[game * 30 : game * 30 + 15])
        p2_scores = checkHands(data[game * 30 + 15 : game * 30 + 30])

        check = 0
        while p1_scores[check] == p2_scores[check]:
            check += 1

        if check == 0:
            p1_val = RANK[p1_scores[check]]
            p2_val = RANK[p2_scores[check]]
        else:
            p1_val = p1_scores[check]
            p2_val = p2_scores[check]

        if p1_val > p2_val:
            p1_wins += 1

    print(f"Player 1 won {p1_wins} times")
    return None


if __name__ == "__main__":
    main()
