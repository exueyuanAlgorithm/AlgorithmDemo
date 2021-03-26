class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for _ in range(32):
            if n % 2 == 1:
                num += 1
            n = n >> 1
        return num


solution = Solution()
print(solution.hammingWeight(0x10001010000000))
