class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False] * (N + 1)
        for i in range(1, N + 1):
            for j in range(1, i // 2 + 1):
                if 0 < j < i and i % j == 0 and dp[i - j] is False:
                    dp[i] = True
                    break
        return dp[-1]


solution = Solution()
print(solution.divisorGame(0))
