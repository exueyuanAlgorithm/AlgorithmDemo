class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        dp = [0] * (len_nums + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len_nums + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]