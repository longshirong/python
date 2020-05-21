"""
删除回文子序列
LeetCode：1332
这里是回文子序列，实际上和回文字串没什么联系，
为空返回0， 是回文的直接删返回1， 不是回文的，先删a再删b返回2
"""


def removePalindromeSub(s: str) -> int:
    if s == "":
        return 0
    if s == s[::-1]:
        return 1
    else:
        return 2


class Solution:
    pass
