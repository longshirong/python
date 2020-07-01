from typing import List

"""
面试题32 - III. 从上到下打印二叉树 III
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> List[List[int]]:
    ans = []
    if not root:
        return ans
    temp = [root]
    value = []
    pre, cur = 1, 0
    while temp:
        node = temp.pop(0)
        value.append(node.val)
        pre -= 1
        if node.left:
            temp.append(node.left)
            cur += 1
        if node.right:
            temp.append(node.right)
            cur += 1
        if pre == 0:
            ans.append(value)
            value = []
            pre = cur
            cur = 0
    for i in range(len(ans)):
        if i % 2 != 0:
            ans[i].reverse()
    return ans


def levelOrder2(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    ans = []
    queue = [root]
    flag = False
    while queue:
        node = []
        value = []
        for v in queue:
            if not v:
                continue
            node.append(v.left)
            node.append(v.right)
            value.append(v.val)
        queue = node
        if flag:
            value.reverse()
        if value:
            ans.append(value)
    return ans


class Solution:
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    levelOrder(node1)
