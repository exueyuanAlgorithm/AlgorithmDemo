class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        zi_left = self.pruneTree(root.left)
        zi_right = self.pruneTree(root.right)
        if not zi_left and not zi_right and root.val == 0:
            return None

        root.left = zi_left
        root.right = zi_right
        return root

