class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def count(self, root, distance):
        if not root:
            return {}, 0
        if not root.left and not root.right:
            return {0: 1}, 0
        left_dict, left_count = self.count(root.left, distance)
        right_dict, right_count = self.count(root.right, distance)
        new_count = 0
        for key_1, value_1 in left_dict.items():
            for key_2, value_2 in right_dict.items():
                if key_1 + key_2 + 2 <= distance:
                    new_count += value_1 * value_2
        new_dict = {}
        for key_1, value_1 in left_dict.items():
            if key_1 + 1 >= distance:
                continue
            new_dict[key_1 + 1] = new_dict.get(key_1 + 1, 0) + value_1
        for key_2, value_2 in right_dict.items():
            if key_2 + 1 >= distance:
                continue
            new_dict[key_2 + 1] = new_dict.get(key_2 + 1, 0) + value_2
        return new_dict, new_count + left_count + right_count


    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        result_dict, new_count = self.count(root, distance)
        return new_count
