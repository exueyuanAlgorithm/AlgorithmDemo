class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = max(dp[0][j - 1], heights[0][j] - heights[0][j - 1])
                elif j == 0:
                    dp[i][j] = max(dp[i - 1][0], heights[i][0] - heights[i - 1][0])
                else:
                    dp[i][j] = min(max(dp[i][j - 1], heights[i][j] - heights[i][j - 1]),
                                   max(dp[i - 1][j], heights[i][j] - heights[i - 1][j]))
        return dp[-1][-1]


solution = Solution()
solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]])
