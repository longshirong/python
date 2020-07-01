"""
221. 最大正方形
https://leetcode-cn.com/problems/maximal-square/
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        dp[i][0] = int(matrix[i][0])
        ans = max(ans, dp[i][0])
    for j in range(n):
        dp[0][j] = int(matrix[0][j])
        ans = max(ans, dp[0][j])
    for i in range(1, m):
        for j in range(1,n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(dp[i][j], ans)
    return ans ** 2


class Solution:
    pass




