def minimumTotal(triangle: List[List[int]]) -> int:
    size = len(triangle)
    for i in range(1, size):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j >= len(triangle[i-1]):
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


class Solution:
    pass