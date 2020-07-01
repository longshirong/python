from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    tails = []
    for n in nums:
        if not tails or n > tails[-1]:
            tails.append(n)
        else:
            l = 0
            r = len(tails) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            tails[loc] = n
    return len(tails)


class Solution:
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums))
