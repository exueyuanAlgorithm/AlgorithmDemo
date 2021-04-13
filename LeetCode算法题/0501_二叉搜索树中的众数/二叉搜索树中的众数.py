class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode_2(self, root):
        if not root:
            return {}
        left_result = self.findMode_2(root.left)
        right_result = self.findMode_2(root.right)
        count = 1
        current_num = root.val
        if current_num in left_result:
            count += left_result.get(current_num, 0)
        if current_num in right_result:
            count += right_result.get(current_num, 0)
        left_result.update(right_result)
        left_result[current_num] = count
        return left_result

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = self.findMode_2(root)
        result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        count = result[0][1]
        result_list = [item[0] for item in result if item[1] == count]
        return result_list
