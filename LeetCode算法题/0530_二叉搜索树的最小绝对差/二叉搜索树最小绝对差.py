class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        shu_list = []
        self.search(root, shu_list)
        min_cha = 1000000000000000
        for i, shu in enumerate(shu_list):
            if i >= 1:
                min_cha = min(min_cha, shu - shu_list[i-1])
        return min_cha

    def search(self, root, shu_list):
        if not root:
            return
        self.search(root.left, shu_list)
        shu_list.append(root.val)
        self.search(root.right, shu_list)