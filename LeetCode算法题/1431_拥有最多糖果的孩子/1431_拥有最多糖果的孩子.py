class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        returnList = []
        for position, candyNum in enumerate(candies):
            if candyNum + extraCandies >= maxCandy:
                returnList.append(True)
            else:
                returnList.append(False)
        return returnList