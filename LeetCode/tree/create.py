from sqlalchemy import null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class createTree:
    def createTree(self, root, lists, i):
        if i < len(lists):
            if lists[i] == null:
                return
            root = TreeNode(lists[i])
            root.left = self.createTree(root.left, lists, 2 * i + 1)
            root.right = self.createTree(root.right, lists, 2 * i + 2)
            return root
        return root
