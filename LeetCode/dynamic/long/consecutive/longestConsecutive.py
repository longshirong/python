"""
128. 最长连续序列
https://leetcode-cn.com/problems/longest-consecutive-sequence/
nums = [100, 4, 200, 1, 3, 2]
answer = 4
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    length = {}
    max_length = 0
    for num in nums:
        if num not in length:
            left = length.get(num - 1, 0)
            right = length.get(num + 1, 0)
            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length
            length[num] = cur_length
            length[num - left] = cur_length
            length[num + right] = cur_length
    return max_length


class Solution:
    nums = [100, 4, 200, 1, 3, 2, 3]
    longestConsecutive(nums)
