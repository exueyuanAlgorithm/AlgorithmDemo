class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def get_longest(self, root):
        if not root:
            return 0, 0
        left_longest_num, left_top_num = self.get_longest(root.left)
        right_longest_num, right_top_num = self.get_longest(root.right)
        new_top_num = 0
        new_top_left = 0
        new_top_right = 0
        if root.left and root.val == root.left.val:
            new_top_num += left_top_num + 1
            new_top_left += left_top_num + 1
        if root.right and root.val == root.right.val:
            new_top_num += right_top_num + 1
            new_top_right += right_top_num + 1
        new_longest_num = max(left_longest_num, right_longest_num, new_top_num)
        result_top_num = max(new_top_left, new_top_right)
        return new_longest_num, result_top_num

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest_num, _ = self.get_longest(root)
        return longest_num
