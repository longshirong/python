from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    sumNums = sum(nums)
    if sumNums % k != 0:
        return False
    sumNums = sumNums // k
    dp = [0] * (sumNums+1)
    dp[0] = 1
    for v in nums:
        for i in range(sumNums, 0, -1):
            if i >= v:
                dp[i] = dp[i] + dp[i-v]
    if dp[-1] >= k:
        return True
    else:
        return False


class Solution:
    nums = [2,2,2,2,3,4,5]
    k = 4
    print(canPartitionKSubsets(nums, k))