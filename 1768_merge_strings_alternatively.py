def mergeAlternately(word1, word2):
    merge = ""
    if len(word1) < len(word2):
        word1 += (" " * (len(word2) - len(word1)))
    else:
        word2 += (" " * (len(word1) - len(word2)))

    for i in range(len(word1)):
        if word1[i] == " ":
            merge += word2[i]
        elif word2[i] == " ":
            merge += word1[i]
        else:
            merge += word1[i] + word2[i]

    return merge

def mergeAlternately2(word1, word2): # ideal solution
    merge = ""
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        merge += word1[i] + word2[i]

    merge += word1[min_len:] + word2[min_len:]
    return merge




print(mergeAlternately2("pq", "abcd"))