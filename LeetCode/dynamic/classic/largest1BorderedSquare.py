"""
1139. 最大的以 1 为边界的正方形
https://leetcode-cn.com/problems/largest-1-bordered-square/
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大正方形子网格，
并返回该子网格中的元素数量。如果不存在，则返回 0。
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
"""
from typing import List


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    left = [[0] * n for _ in range(m)]
    top = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        left[i][0] = grid[i][0]
        max_side = max(grid[i][0], max_side)
        if i > 0 and grid[i][0]:
            top[i][0] = top[i - 1][0] + 1
        else:
            top[i][0] = grid[i][0]

    for j in range(n):
        max_side = max(grid[0][j], max_side)
        top[0][j] = grid[0][j]
        if j > 0 and grid[0][j]:
            left[0][j] = left[0][j - 1] + 1
        else:
            left[0][j] = grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j]:
                top[i][j] = top[i - 1][j] + 1
                left[i][j] = left[i][j - 1] + 1
            for side in range(min(top[i][j], left[i][j]), max_side, -1):
                if left[i - side + 1][j] >= side and top[i][j - side + 1] >= side:
                    max_side = side
    return max_side ** 2


def largest1BorderedSquare2(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    left = [[0] * n for _ in range(m)]
    top = [[0] * n for _ in range(m)]

    max_side = 0
    for i in range(m):
        for j in range(n):
            if i > 0 and grid[i][j]:
                top[i][j] = top[i-1][j] + 1
            else:
                top[i][j] = grid[i][j]
            if j > 0 and grid[i][j]:
                left[i][j] = left[i][j-1] + 1
            else:
                left[i][j] = grid[i][j]
            for side in range(min(top[i][j], left[i][j]), max_side, -1):
                if left[i - side + 1][j] >= side and top[i][j - side + 1] >= side:
                    max_side = side
    return max_side ** 2


class Solution:
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(largest1BorderedSquare(grid))
