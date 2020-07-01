from typing import List
"""
62. 不同路径
https://leetcode-cn.com/problems/unique-paths/
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


class Solution:
    m = 3
    n = 2
    print(uniquePaths(m, n))

