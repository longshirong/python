from typing import List


def findLength(A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    dp = [[0] * n for _ in range(m)]
    max_len = 0
    for i in range(m):
        if A[i] == B[0]:
            dp[i][0] = 1
    for j in range(n):
        if A[0] == B[j]:
            dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    return max_len


class Solution:
    A = [0, 0, 0, 0, 1]
    B = [1, 0, 0, 0, 0]
    print(findLength(A, B))