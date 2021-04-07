class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y
        if Y % 2 == 0:
            middle_num = Y // 2
            if X >= middle_num:
                return X - middle_num + 1
            else:
                return self.brokenCalc(X, middle_num) + 1
        if Y % 2 == 1:
            middle_num = (Y + 1) // 2
            if X >= middle_num:
                return X - middle_num + 2
            else:
                return self.brokenCalc(X, middle_num) + 2

solution = Solution()
print(solution.brokenCalc(1024, 1))