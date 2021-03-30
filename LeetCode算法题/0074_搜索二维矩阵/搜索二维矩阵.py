class Solution(object):

    def search_line(self, num_list, target):
        m = len(num_list)
        middle_position = m // 2
        middle_num = num_list[middle_position]
        if target == middle_num:
            return True
        elif target < middle_num:
            if middle_position <= 0:
                return False
            return self.search_line(num_list[:middle_position], target)
        else:
            if middle_position + 1 >= m:
                return False
            return self.search_line(num_list[middle_position + 1:], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        middle_line = m // 2
        # 判断是否在middle_line中
        left_num = matrix[middle_line][0]
        right_num = matrix[middle_line][n - 1]
        if left_num <= target <= right_num:
            return self.search_line(matrix[middle_line], target)
        else:
            if target < left_num:
                if middle_line <= 0:
                    return False
                return self.searchMatrix(matrix[:middle_line], target)
            else:
                if middle_line + 1 >= m:
                    return False
                return self.searchMatrix(matrix[middle_line + 1:], target)