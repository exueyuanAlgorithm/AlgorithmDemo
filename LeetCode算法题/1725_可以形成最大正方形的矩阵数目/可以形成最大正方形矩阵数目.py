class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_size = 0
        count = 0
        for rectangle in rectangles:
            size = min(rectangle[0], rectangle[1])
            if size == max_size:
                count += 1
            elif size > max_size:
                count = 1
                max_size = size
        return count