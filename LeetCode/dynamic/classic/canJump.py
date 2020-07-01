from typing import List


def canJump(nums: List[int]) -> bool:
    if not nums:
        return True
    size = len(nums)
    dp = [False] * size
    dp[size-1] = True
    temp = size - 1
    for i in range(size-2, -1, -1):
        if temp - nums[i] <= i:
            dp[i] = dp[i+1]
        temp -= nums[i]

    return dp[0]


class Solution:
    nums = [2,0,0]
    print(canJump(nums))