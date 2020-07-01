from typing import List

from sqlalchemy import null

from tree.create import createTree

"""
面试题34. 二叉树中和为某一值的路径
https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这里是从根节点开始， 因此直接从根节点开始逐层把之前节点的值加上就好
def pathSum(root: TreeNode, target: int) -> List[List[int]]:
    if not root:
        return []
    stack = [(root, [root.val])]
    res = []
    while stack:
        node, val = stack.pop()
        if node and not node.left and not node.right and sum(val) == target:
            res.append(val)
        if node.left:
            stack.append((node.left, val + [node.left.val]))
        if node.right:
            stack.append((node.right, val + [node.right.val]))
    return res


class Solution:
    lists = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    root = createTree().createTree(null, lists, 0)
    target = 21
    print(pathSum(root, target))
