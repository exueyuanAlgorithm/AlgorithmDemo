# coding=utf-8

class Solution(object):
    # 上，右，下，左
    dirs = [(0, 1), (1, 0)]
    def isvalid(self, obstacleGrid, position):
        if position[0] < 0 or position[0] >= len(obstacleGrid):
            return False
        if position[1] < 0 or position[1] >= len(obstacleGrid[0]):
            return False
        if obstacleGrid[position[0]][position[1]] == 1:
            return False
        else:
            return True
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

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        startCheck = self.startCheck(obstacleGrid)
        if startCheck is not None:
            return startCheck
        startPosition = (0, 0)
        targetPosition = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        uniquePathNum = 0
        positionDirectionStack = [(startPosition, 0)]
        while positionDirectionStack:
            position, next = positionDirectionStack.pop()
            for i in range(next, len(Solution.dirs)):
                nextposition = position[0] + Solution.dirs[i][0], position[1] + Solution.dirs[i][1]
                if nextposition == targetPosition:
                    positionDirectionStack.append((position, i+1))
                    positionDirectionStack.append((nextposition, 0))
                    print(positionDirectionStack)
                    uniquePathNum += 1
                    positionDirectionStack.pop()
                    break
                if self.isvalid(obstacleGrid, nextposition):
                    positionDirectionStack.append((position, i+1))
                    positionDirectionStack.append((nextposition, 0))
                    break
        return uniquePathNum







obstacleGrid = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]
"""
obstacleGrid = [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
"""
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))