class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        def func(root, k):
            dp = [0] * (k + 1)
            if not root:
                return dp
            left_dp = func(root.left, k)
            right_dp = func(root.right, k)
            dp[0] = max(left_dp) + max(right_dp)
            for i in range(1, k + 1):
                remain_ran = i - 1
                for left_ran in range(0, remain_ran + 1):
                    right_ran = remain_ran - left_ran
                    dp[i] = max(left_dp[left_ran] + right_dp[right_ran] + root.val, dp[i])
            return dp
        return max(func(root, k))

