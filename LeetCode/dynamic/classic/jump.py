from typing import List


def jump(nums: List[int]) -> int:
    size = len(nums)
    step = 0
    maxPos, end = 0, 0
    for i in range(size-1):
        if maxPos >= i:
            maxPos = max(maxPos, nums[i] + i)
            if i == end:
                end = maxPos
                step += 1
    return step


class Solution:
    nums = [2,3,1,1,4]
    print(jump(nums))