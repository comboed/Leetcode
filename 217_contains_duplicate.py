def contains_duplicate(nums: list) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

if __name__ == "__main__":
    nums = [-100, -99, -88, -10, -100]
    print(contains_duplicate(nums))