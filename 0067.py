"""
Name : Maximum Path Sum II
Date created : 04-08-2025
"""

FP = "C:\\Users\\Carlos\\Documents\\Coding\\Project Euler\\ChallengeFiles\\0067_triangle.txt"


def main():

    with open(FP, "r") as f:
        data = f.read()

    
    nums = [[int(num) for num in row.split(" ")] for row in data.split("\n")]

    for i in range(1, len(nums)):
        n = len(nums[i])
        for number in range(0, n):
            if number == 0:
                nums[i][number] += nums[i - 1][number]
            elif number == n - 1:
                nums[i][number] += nums[i - 1][number - 1]
            else:
                nums[i][number] += max(nums[i - 1][number - 1], nums[i - 1][number])
                
    print(f"The maximum sum path starting from the top of the triangle is {max(nums[-1])}")
    return None


if __name__ == "__main__":
    main()