def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    
    if s == " ":
        return 1
    
    best = 1

    for i in range(len(s)):
        substring = s[i]
        count = 1
        for j in range(i + 1, len(s), 1):
            if s[j] not in substring:
                substring += s[j]
                count += 1
                if best < count:
                    best = count
            
            else:
                count = 0
                break
    return best

def lengthOfLongestSubstring2(s):
    if s == "":
        return 0
    
    if s == " ":
        return 1

    substring = ""
    char_index, i, substring_max = 0, 0, 0

    while char_index < len(s):
        if i < len(s) and s[i] not in substring:
            substring += s[i]
            i += 1
            if substring_max < len(substring):
                substring_max = len(substring)
        else:
            substring = ""
            char_index += 1
            i = char_index
        
    return substring_max


print(lengthOfLongestSubstring2("dvdf"))
#print(lengthOfLongestSubstring2("pwwkew"))

# print(sorted("cba"))

# substring = lengthOfLongestSubstring("bbbbb")
# print(substring)