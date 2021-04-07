class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        num1 = sum(A)
        num2 = sum(B)
        sum_all = num1 + num2
        every_one = sum_all // 2
        jiaohuanshu = every_one - num1
        A_set = set(A)
        for item in B:
            if item - jiaohuanshu in A_set:
                return [item-jiaohuanshu, item]