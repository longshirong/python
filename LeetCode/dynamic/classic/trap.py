from typing import List


def trap(height: List[int]) -> int:
    if not height or len(height) < 3:
        return 0
    ans = 0
    size = len(height)
    left = [0] * size
    right = [0] * size
    left[0] = height[0]
    for i in range(1, size):
        left[i] = max(height[i], left[i-1])
    right[size-1] = height[size-1]
    for i in range(size-2, -1, -1):
        right[i] = max(height[i], right[i+1])
    for i in range(1, size-1):
        ans += min(left[i], right[i]) - height[i]
    return ans


class Solution:
    pass
