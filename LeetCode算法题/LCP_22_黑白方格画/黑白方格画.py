from scipy.special import  comb
class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n ** 2 == k:
            return 1
        if k == 0:
            return 1
        sum_ = 0
        for i in range(n + 1):
            for j in range(n + 1):
                xuanze = i * n + j * n - i * j
                if xuanze == k:
                    sum_ += int(comb(n, i) * comb(n, j))
        return sum_



solution = Solution()
print(solution.paintingPlan(2, 0))
