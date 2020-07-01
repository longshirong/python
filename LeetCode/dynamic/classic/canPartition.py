from typing import List


def canPartition(nums: List[int]) -> bool:
    if not nums or len(nums) < 2:
        return False
    sumOfNums = sum(nums)
    if sumOfNums % 2 != 0:
        return False
    sumOfNums = sumOfNums // 2
    dp = [False] * (sumOfNums+1)
    dp[0] = True
    for v in nums:
        for i in range(sumOfNums, 0, -1):
            if i >= v:
                dp[i] = dp[i-v] or dp[i]
    return dp[-1]


class Solution:
    nums = [1, 2, 5]
    print(canPartition(nums))