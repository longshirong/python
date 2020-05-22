from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    :param preorder:
    :param inorder:
    :return:
    """
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]
    inorderIndex = 0
    for i in range(1, len(preorder)):
        preorderVal = preorder[i]
        node = stack[-1]
        if node.val != inorder[inorderIndex]:
            node.left = TreeNode(preorderVal)
            stack.append(node.left)
        else:
            while stack and stack[-1].val == inorder[inorderIndex]:
                node = stack.pop()
                inorderIndex += 1
            node.right = TreeNode(preorderVal)
            stack.append(node.right)

    return root


class Solution:
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    buildTree(preorder,inorder)
