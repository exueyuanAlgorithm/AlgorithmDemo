class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def increasing2(self, root):
        if not root:
            return None, None
        left_root, left_last = self.increasing2(root.left)
        right_root, right_last = self.increasing2(root.right)
        root.left = None
        if left_last and right_root:
            left_last.right = root
            root.right = right_root
            return left_root, right_last
        elif left_last and not right_root:
            left_last.right = root
            root.right = right_root
            return left_root, root
        elif not left_last and right_root:
            root.right = right_root
            return root, right_last
        elif not left_last and not right_root:
            return root, root

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_root, _ = self.increasing2(root)
        return new_root
