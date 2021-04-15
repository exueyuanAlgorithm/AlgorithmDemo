class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda item:item[0])
        max_mianji = -1
        for position, point in enumerate(points):
            if position + 1 >= len(points):
                break
            next_point = points[position + 1]
            mianji = next_point[0] - point[0]
            max_mianji = max(max_mianji, mianji)
        return max_mianji

solution = Solution()
print(solution.maxWidthOfVerticalArea([[8,7], [9,9]]))