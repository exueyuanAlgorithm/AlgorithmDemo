class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_equal(self, s, t):
        if s and not t:
            return False
        if not s and t:
            return False
        if not s and not t:
            return True
        if s.val != t.val:
            return False
        if self.is_equal(s.left, t.left) and self.is_equal(s.right, t.right):
            return True
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s.val == t.val:
            if self.is_equal(s, t):
                return True
        if s.left:
            if self.isSubtree(s.left, t):
                return True
        if s.right:
            if self.isSubtree(s.right, t):
                return True
        return False