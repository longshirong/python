from typing import List

"""
105. 从前序与中序遍历序列构造二叉树
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])
        return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Solution().buildTree(preorder, inorder)
