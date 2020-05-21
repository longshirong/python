"""
回文排列
面试题01.04
"""
import collections


def canPermutePalindrome(s: str) -> bool:
    s = [i for i in s]
    dicts = collections.Counter(s)
    odd = 0
    for i in dicts:
        if dicts[i] % 2 == 1:
            odd += 1
    if odd >= 2 or (odd == 1 and len(s) % 2 == 0):
        return False
    return True


class Solution:
    pass
