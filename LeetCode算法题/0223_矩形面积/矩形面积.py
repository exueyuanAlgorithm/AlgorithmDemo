class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        mianji_1 = (C-A)*(D-B)
        mianji_2 = (G-E)*(H-F)

        bian_1 = self.compute_one_bian(A, C, E, G)
        if bian_1 == 0:
            return mianji_1 + mianji_2
        bian_2 = self.compute_one_bian(B, D, F, H)
        return mianji_1 + mianji_2 - bian_1 * bian_2

    def compute_one_bian(self, A, C, E, G):
        if E >= C or A >= G:
            return 0
        if E >= A and G <= C:
            return G - E
        if A >= E and C <= G:
            return C - A
        if A <= E <= C <= G:
            return C - E
        if E <= A <= G <= C:
            return G - A


solution = Solution()
print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))