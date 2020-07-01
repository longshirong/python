class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "[]"
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    return '[' + ','.join(res) + ']'


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data == '[]':
        return None
    val, i = data[1:-1].split(','), 1
    root = TreeNode(int(val[0]))
    queue = [root]
    while queue:
        node = queue.pop(0)
        if val[i] != "null":
            node.left = TreeNode(int(val[i]))
            queue.append(node.left)
        i += 1
        if val[i] != "null":
            node.right = TreeNode(int(val[i]))
            queue.append(node.right)
        i += 1
    return root


class Codec:
    pass
