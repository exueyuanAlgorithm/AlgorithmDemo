# coding=utf-8

class Solution(object):
    def startCheck(self, obstacleGrid):
        startPosition = (0, 0)
        targetPosition = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        if obstacleGrid[startPosition[0]][startPosition[1]] == 1:
            return 0
        if obstacleGrid[targetPosition[0]][targetPosition[1]] == 1:
            return 0
        if startPosition == targetPosition:
            return 1
        else:
            return None

    def getDpValue(self, dp, i, j):
        if i < 0:
            return 0
        if j < 0:
            return 0
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        startCheck = self.startCheck(obstacleGrid)
        if startCheck is not None:
            return startCheck

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = self.getDpValue(dp, i-1, j) + self.getDpValue(dp, i, j-1)
        return dp[-1][-1]








obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
obstacleGrid = [[0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))