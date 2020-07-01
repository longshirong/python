def longestPalindrome(s: str) -> str:
    if not s or len(s) < 2:
        return s
    size = len(s)
    dp = [[False] * size for _ in range(size)]

    maxLen = 1
    begin = 0
    # 对于自己当前和自己比较
    for i in range(size):
        dp[i][i] = True
    for i in range(size):
        for j in range(i + 1, size):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j + 1]
            if dp[i][j] and j - i + 1 > maxLen:
                maxLen = j - i + 1
                begin = i
    return s[begin:begin + maxLen]


class Solution:
    s = "ababd"
    print(longestPalindrome(s))
