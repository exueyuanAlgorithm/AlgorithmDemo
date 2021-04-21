import operator


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_index, max_number = max(enumerate(nums), key=operator.itemgetter(1))
        tree_node = TreeNode(max_number)
        left_tree = self.constructMaximumBinaryTree(nums[:max_index])
        right_tree = self.constructMaximumBinaryTree(nums[max_index + 1:])
        tree_node.left = left_tree
        tree_node.right = right_tree
        return tree_node
