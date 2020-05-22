# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 使用逆序的中序遍历
        num = 0
        res = 0

        def search(root, k):
            nonlocal num
            nonlocal res
            if root:
                search(root.right, k)
                num += 1
                if num > k:
                    return
                if num == k:
                    res = root.val
                    return
                search(root.left, k)

        search(root, k)
        return res