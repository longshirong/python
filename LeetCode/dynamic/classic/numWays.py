"""
面试题10- II. 青蛙跳台阶问题
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
输入：n = 2
输出：2
"""


def numWays(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    t1, t2 = 1, 2
    for i in range(2, n+1):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    return t2


class Solution:
    n = 3
    print(n)


