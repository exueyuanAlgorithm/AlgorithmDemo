class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        numsLen = len(nums)
        dp = [0] * numsLen
        dp[numsLen-1] = 0
        for i in range(numsLen-2, -1, -1):
            for j in range(i + 1, numsLen):
                if nums[j] < nums[i]:
                    dp[i] = dp[i] + 1
                elif nums[j] == nums[i]:
                    dp[i] = dp[i] + dp[j]
                    break
        return dp

solution = Solution()
print(solution.countSmaller([2, 0, 1]))
