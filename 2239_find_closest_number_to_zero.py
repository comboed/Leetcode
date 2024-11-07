def findClosestNumber(nums) -> int:
    closest = abs(nums[0]) # calculate first idstance

    for i in range(1, len(nums), 1):
        distance = abs(nums[i])
        if distance < closest:
            closest = distance

    if closest in nums:
        return closest
    return 0 - closest

# print(findClosestNumber([-1000, -1000]))
print(findClosestNumber([2, -1, 1]))
# print(findClosestNumber([-100000,-100000]))