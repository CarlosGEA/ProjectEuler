"""
Name : Passcode Derivation
Date created : 20-08-2025
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0079_keylog.txt"


class ListNode:
    def __init__(self, val=0, next=None, seen=False):
        self.val = val
        self.next = next
        self.seen = seen


def main():

    with open(FP, "r") as f:
        data = f.read()

    numbers = data.split("\n")[:-1]
    start = ListNode("-1")

    for num in numbers:
        dummy = start
        for i in range(len(num)):
            digit = num[i]
            if i == 2:
                next_digit = "-1"
            else:
                next_digit = num[i + 1]

            while dummy.val != digit and dummy.next and dummy.next.val != next_digit:
                dummy = dummy.next

            if dummy.val == digit:
                continue
            nxt = dummy.next
            dummy.next = ListNode(digit)
            dummy = dummy.next
            dummy.next = nxt

    for num in numbers:
        dummy = start
        for digit in num:
            while dummy.val != digit:
                dummy = dummy.next
            dummy.seen = True

    res = []
    head = start
    while head:
        if head.seen:
            res.append(head.val)
        head = head.next
    print(f"The shortest possible passcode is {''.join(res)}")

    return None

# 583906758391 -> attempt with this

if __name__ == "__main__":
    main()
