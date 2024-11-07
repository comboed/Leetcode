def findDisappearedNumbers(nums: list):
    missing = []
    nums.sort()
    nums_set = set(nums)

    for i in range(len(nums_set)):
        if nums_set.pop() != i + 1:
            missing.append(i + 1)

    return missing



if __name__ == "__main__":
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))