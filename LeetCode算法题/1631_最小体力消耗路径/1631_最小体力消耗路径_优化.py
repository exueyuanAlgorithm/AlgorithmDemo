from data import data


class Solution(object):
    def search_insert(self, new_node_list, target):
        left = 0
        right = len(new_node_list) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if new_node_list[mid][0] == target[0]:
                return mid
            elif new_node_list[mid][0] < target[0]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def append_to_list(self, new_node_list, tuple_data):
        weizhi = self.search_insert(new_node_list, tuple_data)
        new_node_list.insert(weizhi, tuple_data)

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        dp = [[0] * n for _ in range(m)]
        fangxiang_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        already_node_set = set()
        already_node_set.add((0, 0))
        new_node_list = [(0, (0, 0), ())]
        while True:
            if not new_node_list:
                break
            min_distance, cur_point, pre_point = new_node_list.pop(0)
            if pre_point:
                if cur_point in already_node_set:
                    continue
                already_node_set.add(cur_point)
                dp[cur_point[0]][cur_point[1]] = max(dp[pre_point[0]][pre_point[1]], min_distance)
                if cur_point[0] == len(heights) - 1 and cur_point[1] == len(heights[0]) - 1:
                    break
            for fangxiang in fangxiang_list:
                new_node_x = cur_point[0] + fangxiang[0]
                new_node_y = cur_point[1] + fangxiang[1]
                if new_node_x < 0 or new_node_y < 0 or new_node_x >= m or new_node_y >= n:
                    continue
                if (new_node_x, new_node_y) in already_node_set:
                    continue
                distance = abs(heights[new_node_x][new_node_y] - heights[cur_point[0]][cur_point[1]])
                # 排序增加
                add_data = (distance, (new_node_x, new_node_y), cur_point)
                self.append_to_list(new_node_list, add_data)
        return dp[-1][-1]


solution = Solution()
# data = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(solution.minimumEffortPath(data))
