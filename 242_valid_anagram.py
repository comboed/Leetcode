from collections import Counter

# Use coutner to count the number of hashable characters
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    C = Counter(s)
    D = Counter(t)

    for c in s:
        if C[c] != D[c]:
            return False
    return True

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)