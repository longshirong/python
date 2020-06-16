from typing import List

"""
15. 三数之和
https://leetcode-cn.com/problems/3sum/
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        k = n - 1
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            while j < k and nums[j] + nums[k] > target:
                k -= 1
            if j == k:
                break
            if nums[j] + nums[k] == target:
                res.append([nums[i], nums[j], nums[k]])
    return res


class Solution:
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
