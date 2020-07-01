from typing import List
"""
300. 最长上升子序列
https://leetcode-cn.com/problems/longest-increasing-subsequence/

nums = [10,9,2,5,3,7,101,18]
answer : 4
"""


def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    size = len(nums)
    dp = [1] * size
    for i in range(1, size):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


class Solution:
    pass
