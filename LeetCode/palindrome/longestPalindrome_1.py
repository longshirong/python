"""
构造最长回文串，区分大小写
LeetCode：409
记住A 和 a的ASCLL码，A是65， a是97
python里没有char的说法不能直接减，使用ord将字母转为数字，使用chr将数字转为字母
"""


def longestPalindrome(s: str) -> int:
    # ASCLL码里A是65，a是97，显然这中间还有其他符号
    chars = [0] * 58
    ans = 0
    for i in s:
        num = ord(i) - 65
        chars[num] += 1
    for i in chars:
        ans += i - (i & 1)
    if ans < len(s):
        return ans + 1
    else:
        return ans


class Solution:
    s = "abccccdd"
    ans = longestPalindrome(s)
    print(ans)
