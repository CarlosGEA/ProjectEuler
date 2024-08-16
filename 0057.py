"""
Name : 
Date created : 16-08-2024
"""

MAX_ITER = 1000


def main():

    cur_iter = 1
    count = 0

    num_0, denom_0 = 3, 2
    # denom_0 = 2
    num_1, denom_1 = 7, 5
    # denom_1 = 5

    for cur_iter in range(1, MAX_ITER):
        num_1, num_0 = 2 * num_1 + num_0, num_1
        denom_1, denom_0 = 2 * denom_1 + denom_0, denom_1
    # while cur_iter < MAX_ITER:
    #     dummy_num = num_1
    #     dummy_denom = denom_1

    #     num_1 = 2 * num_1 + num_0
    #     num_0 = dummy_num

    #     denom_1 = 2 * denom_1 + denom_0
    #     denom_0 = dummy_denom
        if len(str(num_1)) > len(str(denom_1)):
            count += 1
        cur_iter += 1

    print(f"The answer is {count}")
    return None


# new numerator and denominator * 2 of current + one previous


if __name__ == "__main__":
    main()
