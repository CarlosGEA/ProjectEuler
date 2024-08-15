"""
Name : Poker Hands
Date created : 15-08-2024
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0054_poker.txt"

"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""

RANK = {"HC": 0, "OP": 1, "TP": 2, "TOK": 3, "S": 4, "F": 5, "FH": 6, "FOK": 7, "SF": 8, "RF": 9}


def checkStraightFlush(nums):
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
    cards = cards.split(" ")[:-1]
    value, suits = map(list, zip(*[(i[0], i[1]) for i in cards]))
    nums = valueToNums(value)
    # for idx, num in enumerate(nums):
    #     if num == "T":
    #         nums[idx] = "10"
    #     elif num == "J":
    #         nums[idx] = "11"
    #     elif num == "Q":
    #         nums[idx] = "12"
    #     elif num == "K":
    #         nums[idx] = "13"
    #     elif num == "A" and "".join(sorted(nums)) == "2345A":
    #         nums[idx] = "1"
    #     elif num == "A":
    #         nums[idx] = "14"

    # sorted_nums = sorted([int(i) for i in nums])
    print(nums, suits)

    if len(set(suits)) == 1:
        if checkStraightFlush(nums):
            if nums[-1] == 14:
                return ["RF"]
            else:
                return ["SF", nums[-1]]
        return ["F"] + nums[::-1]

    return None


def main():
    with open(FP, "r") as f:
        data = f.read()
    games = 1000
    for game in range(games):
        p1_hand = data[game * 30 : game * 30 + 15]
        p2_hand = data[game * 30 + 15 : game * 30 + 30]

        # p1_val = checkHands(p1_hand)
        # p2_val = checkHands(p2_hand)
        break
        # if p1_val == p2_val:
        #     p1_val = checkHands()
    checkHands(data[30:45])
    # print(checkHands("TC 8C AC 3C 5C "))

    return None


if __name__ == "__main__":
    main()
