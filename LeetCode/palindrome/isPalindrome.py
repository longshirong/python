"""
判断一个整数是否为回文数
LeetCode：9
实际上把它转成列表形式的，直接判断即可
"""


def isPalindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


class Solution:
    pass
