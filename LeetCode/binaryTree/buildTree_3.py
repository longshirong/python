"""
106. 从中序与后序遍历序列构造二叉树
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        x = postorder.pop()
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:])

        return node
