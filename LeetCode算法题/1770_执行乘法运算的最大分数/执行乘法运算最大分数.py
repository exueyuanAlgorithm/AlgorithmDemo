class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        xuanze_num = len(multipliers)
        dp = [[0] * (xuanze_num + 1) for _ in range(xuanze_num+1)]
        dp[0][1] = 3
        max_num = -99999999999999
        for i in range(xuanze_num + 1):
            for j in range(xuanze_num + 1):
                if i + j > xuanze_num:
                    continue
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + nums[-j] * multipliers[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + nums[i - 1] * multipliers[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1],
                                   dp[i][j - 1] + nums[-j] * multipliers[i + j - 1])
                if i + j == xuanze_num:
                    max_num = max(max_num, dp[i][j])
        return max_num

solution = Solution()
print(solution.maximumScore([3, 2, 5, 8, 7, 8], [3, 2, 1]))
