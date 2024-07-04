"""
Name : Reciprocal Cycles
Date created : 03-07-2024
"""

N = 1000


def fractionToDecimal(numr, denr):

    res = ""
    mp = {}

    rem = numr % denr

    while (rem != 0) and (rem not in mp):
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // denr
        res += str(res_part)
        rem = rem % denr

    if rem == 0:
        return ""
    else:
        return res[mp[rem] :]


def main():
    rec_len = 0
    rec_num = 0
    for num in range(1, N):
        rec = fractionToDecimal(1, num)
        if len(rec) > rec_len:
            rec_len = len(rec)
            rec_num = num
    print(f"The largest recurring fraction has {rec_num} as its denominator, length {rec_len}")
    return None


if __name__ == "__main__":
    main()
