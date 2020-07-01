from typing import List
"""
416. 分割等和子集
https://leetcode-cn.com/problems/partition-equal-subset-sum/
输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
"""


def canPartition(nums: List[int]) -> bool:
    val = sum(nums)
    if not nums or val % 2 != 1:
        return 0
    size = len(nums)
    val = val // 2
    dp = [False] * (val+1)
    dp[0] = True
    for i in range(size):
        for j in range(val, 0, -1):
            if j >= nums[i]:
                dp[j] = dp[j] or dp[j-nums[i]]
    return dp[-1]


class Solution:
    nums = [1, 5, 11, 5]
    canPartition(nums)
