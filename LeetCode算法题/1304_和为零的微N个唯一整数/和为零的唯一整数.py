class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        numList = []
        if n % 2 != 0:
            numList.append(0)
            n = n-1
        for i in range(1, n//2+1):
            numList.append(i)
            numList.append(-i)
        return numList

solution = Solution()
print(solution.sumZero(4))