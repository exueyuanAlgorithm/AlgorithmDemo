class Solution(object):
    def largestSumOfAverages_dict(self, A, K, cache_dict):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if (tuple(A), K) in cache_dict:
            return cache_dict[(tuple(A), K)]
        if not A and K == 0:
            return 0
        length = len(A)
        if K > length or K <= 0:
            return None

        score = 0
        for i in range(1, length + 1):
            A_ = A[:i]
            if (tuple(A_), i) in cache_dict:
                avg_1 = cache_dict[(tuple(A_), 1)]
            else:
                avg_1 = sum(A_) / i
                cache_dict[(tuple(A_), 1)] = avg_1
            avg_2 = self.largestSumOfAverages_dict(A[i:], K - 1, cache_dict)
            if avg_2 is not None:
                avg = avg_1 + avg_2
                if avg > score:
                    score = avg
        cache_dict[(tuple(A), K)] = score
        return score

    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        return self.largestSumOfAverages_dict(A, K, {})


solution = Solution()
print(solution.largestSumOfAverages([9, 1, 2, 3, 9], 3))
