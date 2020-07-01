class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftVal = max(maxGain(node.left), 0)
            rightVal = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceVal = node.val + leftVal + rightVal

            # 更新答案
            self.maxSum = max(self.maxSum, priceVal)

            # 返回节点的最大贡献值
            return node.val + max(leftVal, rightVal)

        maxGain(root)
        return self.maxSum

