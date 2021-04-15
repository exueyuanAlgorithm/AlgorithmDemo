class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        xiabiao = -1
        min_juli = 99999999999999
        for position, point in enumerate(points):
            x_1, y_1 = point
            if x == x_1 or y == y_1:
                juli = abs(x-x_1) + abs(y-y_1)
                if juli < min_juli:
                    xiabiao = position
                    min_juli = juli
                if juli == 0:
                    break
        return xiabiao