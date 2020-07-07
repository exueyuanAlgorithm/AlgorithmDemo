class Solution:
    def getDpIJ(self, dp, i, j):
        if i < 0 or j < 0:
            return 0
        return dp[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*n for _ in range(m)]
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if text1[i] == text2[j]:
                    dp[i][j] = self.getDpIJ(dp, i-1, j-1) + 1
                else:
                    dp[i][j] = max(self.getDpIJ(dp, i-1, j), self.getDpIJ(dp, i, j-1))
        return dp[-1][-1]

solution = Solution()
print(solution.longestCommonSubsequence("a", "aaa"))