def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            ans = max(ans, dp[i][j])
    return ans


class Solution:
    text1 = "oxcpqrsvwf"
    text2 = "shmtulqrypy"
    print(longestCommonSubsequence(text1,text2))