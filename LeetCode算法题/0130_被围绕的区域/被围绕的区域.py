class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        fangxiang_list = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        already_search_point = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in already_search_point:
                    continue
                if board[i][j] == "X":
                    continue
                search_points = [(i, j)]
                already_search_point.add((i, j))
                z = 0
                is_can_tu_se = True
                while z < len(search_points):
                    search_point = search_points[z]
                    search_point_x = search_point[0]
                    search_point_y = search_point[1]
                    z += 1
                    for fangxiang_x, fangxiang_y in fangxiang_list:
                        new_x = search_point_x + fangxiang_x
                        new_y = search_point_y + fangxiang_y
                        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                            is_can_tu_se = False
                            continue
                        if (new_x, new_y) in already_search_point:
                            continue
                        if board[new_x][new_y] == "O":
                            already_search_point.add((new_x, new_y))
                            search_points.append((new_x, new_y))
                if is_can_tu_se:
                    for points_x, points_y in search_points:
                        board[points_x][points_y] = "X"


solution = Solution()
solution.solve([["O","X","O"],["X","O","X"],["O","X","O"]])
