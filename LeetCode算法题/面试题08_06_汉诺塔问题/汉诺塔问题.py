class Solution(object):
    def hanota_num(self, A, B, C, num):
        if num == 0:
            return
        self.hanota_num(A, C, B, num - 1)
        pop_num = A.pop()
        C.append(pop_num)
        self.hanota_num(B, A, C, num - 1)

    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        self.hanota_num(A, B, C, len(A))
