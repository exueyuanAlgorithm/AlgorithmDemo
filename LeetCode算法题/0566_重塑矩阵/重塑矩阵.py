class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        new_nums = [[0] * c for _ in range(r)]
        new_x = 0
        new_y = 0
        for i in range(m):
            for j in range(n):
                num = nums[i][j]
                new_nums[new_x][new_y] = num
                if new_y + 1 < c:
                    new_y += 1
                else:
                    new_y = 0
                    new_x += 1
        return new_nums
