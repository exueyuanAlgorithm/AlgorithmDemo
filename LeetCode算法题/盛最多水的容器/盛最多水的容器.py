class Solution(object):
    def getMaxArea(self, height, i, j):
        return (j - i) * min(height[i], height[j])

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = self.getMaxArea(height, i, j)
        while True:
            while height[i] <= height[j]:
                i += 1
                if i == j:
                    return maxArea
                tempArea = self.getMaxArea(height, i, j)
                if maxArea < tempArea:
                    maxArea = tempArea
            while height[i] > height[j]:
                j -= 1
                if i == j:
                    return maxArea
                tempArea = self.getMaxArea(height, i, j)
                if maxArea < tempArea:
                    maxArea = tempArea


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
