class Solution(object):
    def clumsy(self, n):
        """
        :type N: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3*2//1
        if n == 4:
            return 4*3//2+1
        if n > 4:
            return n * (n-1)//(n-2) + (n-3) - self.change_clumsy(n-4)

    def change_clumsy(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3*2//1
        if n == 4:
            return 4*3//2-1
        if n > 4:
            return n * (n-1) //(n-2) - (n-3) + self.change_clumsy(n-4)


solution = Solution()
result = solution.clumsy(8)
print(result)