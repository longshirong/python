import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque
        queue.append(root)
        ans = []
        while queue:
            size = len(queue)
            temp_node = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                temp_node.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if temp_node:
                ans.append(temp_node)
        return ans

