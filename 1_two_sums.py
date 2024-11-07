def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):  
        complement = target - nums[i] # complement meaning the number if added to another number in nums
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    
    # :
    #     if nums[i] + nums[i + 1] == target:
    #         return [i, i + 1]

print(twoSum([3, 2, 4], 6))