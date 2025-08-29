a = set("x3nzwiuf52")
print(a)


result = ""
if not result:
    print("EMPTY")


def iter_digits(counts: list[int], used: int):
    if len(counts) == 10:
        yield counts
    else:
        lower = 0 if len(counts) < 9 else 7 - used
        # lower = 0 if len(counts) < 9 else 3 - used
        upper = 8 - used
        # upper = 4 - used
        for k in range(lower, upper):
            counts.append(k)
            yield from iter_digits(counts, used + k)
            counts.pop()


count = 0
for ks in iter_digits([], 0):
    count += 1
    res = 0
    start = 0
    for d, kd in enumerate(ks):
        for i in range(start, kd + start):
            res += d * 10**i
        start += kd
    # print(res)

print(count)
# break

import math



"""
100 - use eq x + y > 10 ^ 12
x / 10 ^ 12 + x - 1 / 10 ^ 12 - 1 = 0.5
start at 10 ^ 12 and work upwards

Also 94,95,99



"""