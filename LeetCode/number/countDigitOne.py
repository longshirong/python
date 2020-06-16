"""
面试题43. 1～n整数中1出现的次数
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
输入：n = 12
1,10,11,12
输出：5
"""


def countDigitOne(n: int) -> int:
    digit, res = 1, 0
    high, cur, low = n // 10, n % 10, 0

    while high != 0 or cur != 0:
        if cur == 0:
            res += high * digit
        elif cur == 1:
            res += high * digit + low + 1
        else:
            res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res


class Solution:
    n = 12
    print(countDigitOne(n))
