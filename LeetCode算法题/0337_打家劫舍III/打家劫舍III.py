class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def func(node):
            if not node:
                return 0, 0
            left_dao_max, left_not_dao_max = func(node.left)
            right_dao_max, right_not_dao_max = func(node.right)
            # 如果盗取的话
            dao_max = left_not_dao_max + right_not_dao_max + node.val
            not_dao_max = max(left_dao_max, left_not_dao_max) + max(right_dao_max, right_not_dao_max)
            return dao_max, not_dao_max

        return max(func(root))
