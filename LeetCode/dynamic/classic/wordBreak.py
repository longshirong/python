from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    size = len(s)
    words = set(wordDict)
    dp = [False] * (size+1)
    dp[0] = True
    for i in range(size+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                #break
    return dp[-1]


class Solution:
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s,wordDict))