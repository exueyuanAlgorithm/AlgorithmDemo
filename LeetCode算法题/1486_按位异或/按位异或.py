class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        he = 0
        for i in range(n):
            shu = start + 2 * i
            he = he ^ shu
        return he
