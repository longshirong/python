"""
面试题44. 数字序列中某一位的数字
https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
输入：n = 3
输出：3
"""


def findNthDigit(n: int) -> int:
    if n <= 9:
        return n
    digit = 1
    count = 9
    start = 1
    while count < n:
        digit += 1
        start *= 10
        n -= count
        count = digit*9*start
    # 算出在1000开始后第几个数里，这里的数是指完整的四位数
    num = start + (n-1)//digit
    index = (n-1) % digit
    num = str(num)
    return int(num[index])


class Solution:
    n = 26
    print(findNthDigit(n))






