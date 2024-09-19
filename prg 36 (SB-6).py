def wordBreak(s, wordDict):
    word_set = set(wordDict)  
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break 
    return dp[n]
wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
s1 = "ilike"
s2 = "ilikesamsun"

print(wordBreak(s1, wordDict))  
print(wordBreak(s2, wordDict))  
