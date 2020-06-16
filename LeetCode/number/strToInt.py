"""
面试题67. 把字符串转换成整数
https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
"""


def strToInt(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    int_max, boundary, int_min = 2 ** 31 - 1, 2 ** 31 // 10, -2 ** 31
    res, sign, i = 0, 1, 0
    if s[0] == '+':
        i = 1
    if s[0] == '-':
        sign = -1
        i = 1
    for v in s[i:]:
        if not '0' <= v <= '9':
            return 0
        if res > boundary or res == boundary and v > '7':
            return int_max if sign == 1 else int_min
        res = res * 10 + ord(v) - ord('0')
    return sign * res


class Solution:
    s = '   042'
    print(strToInt(s))
