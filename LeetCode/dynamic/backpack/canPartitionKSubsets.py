"""
698. 划分为k个相等的子集
https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

"""


def canPartitionKSubsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target: return False

    memo = [None] * (1 << len(nums))
    memo[-1] = True

    def search(used, todo):
        if memo[used] is None:
            targ = (todo - 1) % target + 1
            memo[used] = any(search(used | (1 << i), todo - num)
                             for i, num in enumerate(nums)
                             if (used >> i) & 1 == 0 and num <= targ)
        return memo[used]

    return search(0, target * k)


class Solution(object):
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    canPartitionKSubsets(nums, k)
