def two_sums(nums: list, target: int):
    nums_dict = {}
    
    for i in range(len(nums)):
        nums_dict[nums[i]] = i # store index


    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and nums_dict[complement] != i:
            return [i, nums_dict[complement]]
        
    # return None

print(two_sums([1,3,4,2], 6))