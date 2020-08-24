class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(abs(x))
        returnNum = int(a[::-1])
        if x < 0:
            returnNum = - returnNum
        if returnNum < (- 2 ** 31) or returnNum > (2 ** 31 - 1):
            return 0
        return returnNum

solution = Solution()
print(solution.reverse(1534236469))