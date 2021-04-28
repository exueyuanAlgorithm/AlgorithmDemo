import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            if i * i + j * j == c:
                return True
            while i <= j and i * i + j * j < c:
                i += 1
            while i <= j and i * i + j * j > c:
                j -= 1
        return False

solution = Solution()
print(solution.judgeSquareSum(4))
