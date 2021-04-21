class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        indice_x_dict = {}
        indice_y_dict = {}
        for x, y in indices:
            indice_x_dict[x] = indice_x_dict.get(x, 0) + 1
            indice_y_dict[y] = indice_y_dict.get(y, 0) + 1
        x_num = 0
        y_num = 0
        for key, item in indice_x_dict.items():
            if item % 2 == 1:
                x_num += 1
        for key, item in indice_y_dict.items():
            if item % 2 == 1:
                y_num += 1
        return x_num * n + y_num * m - x_num * y_num * 2


