from collections import defaultdict

def groupAnagrams(strs: list):
    matrix = []

    while (len(strs) > 0):
        strings = []

        for potential_string in strs:
            if len(potential_string) == len(strs[0]):
                strings.append(potential_string)
        
        chars = []
        occurences = {}

        for string in strings:
            occurences[string] = {}
            string_chars = occurences[string]

            for char in string:
                if char not in string_chars:
                    string_chars[char] = 1
                    chars.append(char)
                else:
                    string_chars[char] += 1

            occurences[string] = string_chars

        done = []
        for i in range(len(strings)):
            anagrams = []
            if strings[i] not in done:
                done.append(strings[i])
                anagrams.append(strings[i])

                for j in range(len(strings)):
                    if i != j and occurences[strings[i]] == occurences[strings[j]]:
                        anagrams.append(strings[j])
                        done.append(strings[j])

                if len(anagrams) > 0:
                    matrix.append(anagrams)
                else:
                    matrix.append([strings[i]])

        for string in strings:
            strs.remove(string)

    return matrix

def groupAnagrams2(strs):
    anagrams = {}
    anagrams = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
        
    return anagrams.values()


def groupAnagrams3(strs):
    anagrams = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        anagrams[tuple(count)].append(word)

    return anagrams.values()

#ddd = ["h", "h", "h", "h"]
#ddd = ["act","pots","tops","cat","stop","hat"]
ddd = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
print(groupAnagrams3(ddd))
