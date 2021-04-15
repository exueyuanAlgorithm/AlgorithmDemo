class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        i = m - 1
        j = n - 1
        z = m + n - 1
        while True:
            if z < 0:
                break
            if j < 0:
                return
            if i < 0:
                x2 = B[j]
                A[z] = x2
                j -= 1
                z -= 1
                continue
            x1 = A[i]
            x2 = B[j]
            if x1 <= x2:
                A[z] = x2
                j -= 1
                z -= 1
            else:
                A[z] = x1
                i -= 1
                z -= 1