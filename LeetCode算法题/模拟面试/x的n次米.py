class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            juduizhiN = n
        else:
            juduizhiN = -n
        ji = 1
        for _ in range(juduizhiN):
            ji = ji*x
        if n < 0:
            ji = 1/ji
        return ji

solution = Solution()
# print(solution.myPow(2.0, 10))
print(solution.myPow(0.00001, 2147483647))