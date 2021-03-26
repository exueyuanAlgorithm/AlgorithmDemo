class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i_set = set()
        j_set = set()
        for i, line in enumerate(matrix):
            for j, num in enumerate(line):
                if num == 0:
                    i_set.add(i)
                    j_set.add(j)
        for i, line in enumerate(matrix):
            for j, num in enumerate(line):
                if i in i_set or j in j_set:
                    matrix[i][j] = 0