class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        daoyu_set = set()
        max_mianji = 0
        for i, line in enumerate(grid):
            for j, num in enumerate(line):
                if (i, j) in daoyu_set:
                    continue
                if num == 0:
                    continue
                max_mianji_2, daoyu_set_2 = self.search(grid, i, j)
                max_mianji = max(max_mianji, max_mianji_2)
                daoyu_set = daoyu_set | daoyu_set_2
        return max_mianji

    def search(self, grid, i, j):
        daoyu_set = set()
        daoyu_set.add((i, j))
        daoyu_list = [(i, j)]
        fangxiang = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        position = 0
        while True:
            if position >= len(daoyu_list):
                return len(daoyu_list), daoyu_set
            i, j = daoyu_list[position]
            for i_fang, j_fang in fangxiang:
                new_i = i + i_fang
                new_j = j + j_fang
                if new_i < 0 or new_i >= len(grid):
                    continue
                if new_j < 0 or new_j >= len(grid[0]):
                    continue
                if (new_i, new_j) in daoyu_set:
                    continue
                if grid[new_i][new_j] == 1:
                    daoyu_set.add((new_i, new_j))
                    daoyu_list.append((new_i, new_j))
            position += 1


solution = Solution()
print(solution.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
