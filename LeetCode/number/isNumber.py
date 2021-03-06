"""
面试题20. 表示数值的字符串
https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。
"""


def isNumber(s: str) -> bool:
    s = s.strip()
    met_dot = met_e = met_digit = False

    for i, char in enumerate(s):
        if char in ('+', '-'):
            if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                return False
        elif char == '.':
            if met_dot or met_e:
                return False
            met_dot = True
        elif char == 'e' or char == 'E':
            if met_e or not met_digit:
                return False
            met_e, met_digit = True, False  # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
        elif char.isdigit():
            met_digit = True
        else:
            return False
    return met_digit


class Solution:
    s = "1e3"
    print(isNumber(s))