# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def get_yezi_list(self, root):
        if not root:
            return list()
        if not root.left and not root.right:
            return [root.val]
        left_list = list()
        if root.left:
            left_list = self.get_yezi_list(root.left)
        right_list = list()
        if root.right:
            right_list = self.get_yezi_list(root.right)
        left_list.extend(right_list)
        return left_list

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list_1 = self.get_yezi_list(root1)
        list_2 = self.get_yezi_list(root2)
        if list_1 == list_2:
            return True
        else:
            return False