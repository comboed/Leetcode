from collections import Conuter

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    My original way
    """
    C = dict(Counter(nums))
    print(C)
    for i in range(k):
        n = max(C, key = C.get)
        freq.append(n)
        C.pop(n)
    return freq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    Using bubble sort method
    """
    C = Counter(nums)
    
    freq = [[] for _ in range(len(nums) + 1)]
    
    for num in C:
        freq[C[num]].append(num)
    
    res = []
    for i in range(len(freq) - 1, -1, -1):
        for j in range(len(freq[i])):
            res.append(freq[i][j])
            
            if len(res) == k:
                return res