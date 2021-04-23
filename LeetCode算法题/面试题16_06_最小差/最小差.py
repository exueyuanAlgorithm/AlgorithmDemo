class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        a.sort()
        b.sort()
        i = 0
        j = 0
        min_result = 999999999999
        while True:
            if i >= len(a) or j >= len(b):
                break
            item1 = a[i]
            item2 = b[j]
            if item1 == item2:
                return 0
            elif item1 > item2:
                j += 1
            elif item1 < item2:
                i += 1
            distance = abs(item1 - item2)
            if distance < min_result:
                min_result = distance
        return min_result
