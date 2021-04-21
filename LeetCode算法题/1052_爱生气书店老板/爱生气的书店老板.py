class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        sum_ = 0
        for customer, grump in zip(customers, grumpy):
            if grump == 0:
                sum_ += customer
        if X > len(customers):
            X = len(customers)
        max_sum = 0
        for i in range(len(customers) - X + 1):
            sum_2 = sum_
            for j in range(i, i+X):
                if grumpy[j] == 1:
                    sum_2 += customers[j]
            if sum_2 > max_sum:
                max_sum = sum_2
        return max_sum





solution = Solution()
solution.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3)
