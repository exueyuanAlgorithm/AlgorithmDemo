class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        sum_ = 0
        if low <= root.val <= high:
            sum_ += root.val
        sum_ += self.rangeSumBST(root.left, low, high)
        sum_ += self.rangeSumBST(root.right, low, high)
        return sum_