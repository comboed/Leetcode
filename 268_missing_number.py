def missingNumber2(nums: list):
    n = [-1] * (len(nums) + 1)
    for num in nums:
        n[num] = num

    for i in range(len(n)):
        if n[i] == -1:
            return i

if __name__ == "__main__":
    nums = [0, 1, 2, 4]
    print(missingNumber2(nums))
    # print(missingNumber(nums))