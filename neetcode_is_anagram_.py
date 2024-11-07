def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    occurences = {}
    for char in s:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1
    
    for char in t:
        if char in occurences:
            occurences[char] -= 1
            if occurences[char] == 0 :
                occurences.pop(char)
        else:
            return False

    return len(occurences) == 0


    # chars = []
    
    # for char in s:
    #     chars.append(char)

    # for char in t:
    #     if char in chars:
    #         chars.remove(char)

    # return len(chars) == 0

print(isAnagram("xx", "xx"))
    

    # if len(s) != len(t):
    #     return False

    # for char in s:
    #     if char not in t:
    #         return False
    # return True