class Solution(object):
    def findSquare(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        already_set = []
        max_bianchang = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    continue
                if (i, j) in already_set:
                    continue
                bianchang = 1
                while True:
                    bianchang += 1
                    # right_position =


