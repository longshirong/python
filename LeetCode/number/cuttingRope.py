"""
面试题14- II. 剪绳子 II
https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
输入: 11
输出: 54
解释: 54=3x3x3x2
"""


def cuttingRope(n: int) -> int:
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = 1
    while n > 4:
        res *= 3
        res %= 1000000007
        n -= 3
    return (res * n) % 1000000007


class Solution:
    n = 11
    print(cuttingRope(n))
