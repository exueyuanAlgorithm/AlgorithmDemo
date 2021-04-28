import copy


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        M_ = copy.deepcopy(M)
        m = len(M)
        n = len(M[0])
        direction_list = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        for i, line in enumerate(M):
            for j, item in enumerate(line):
                count = 0
                sum_ = 0
                for direction_x, direction_y in direction_list:
                    new_i = i + direction_x
                    new_j = j + direction_y
                    if new_i < 0 or new_i >= m:
                        continue
                    if new_j < 0 or new_j >= n:
                        continue
                    count += 1
                    sum_ += M[new_i][new_j]
                average = sum_ // count
                M_[i][j] = average
        return M_
