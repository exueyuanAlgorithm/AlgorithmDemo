import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        bianchang = int(math.sqrt(area))
        for i in range(bianchang, 0, -1):
            if area % i == 0:
                j = area // i
                return [j, i]
