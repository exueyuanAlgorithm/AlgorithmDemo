


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys
class Solution(object):
    def check_BST(self, root, max_num=sys.maxsize, min_num=-sys.maxsize - 1):
        if not root:
            return True
        if root.val <= min_num or root.val >= max_num:
            return False
        if not self.check_BST(root.left, max_num=root.val, min_num=min_num):
            return False
        if not self.check_BST(root.right, max_num=max_num, min_num=root.val):
            return False
        return True


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_BST(root)

