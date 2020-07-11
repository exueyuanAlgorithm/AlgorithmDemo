import math
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n+1)
        for i in range(1, n+1):
            needJian = int(math.sqrt(i))
            for j in range(1, needJian+1):
                if not dp[i - j**2]:
                    dp[i] = True
                    break
        return dp[-1]




solution = Solution()
print(solution.winnerSquareGame(8))
