
import heapq


class HeapQNode(object):
    def __init__(self, min_distance, cur_point, pre_point):
        self.min_distance = min_distance
        self.cur_point = cur_point
        self.pre_point = pre_point

    def __lt__(self, other):
        if self.min_distance < other.min_distance:
            return True
        else:
            return False


class Solution(object):

    def append_to_list(self, new_node_list, heapq_node: HeapQNode):
        heapq.heappush(new_node_list, heapq_node)

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
        new_node_list = [HeapQNode(0, (0, 0), ())]
        while True:
            if not new_node_list:
                break
            heapq_node = heapq.heappop(new_node_list)

            min_distance, cur_point, pre_point = heapq_node.min_distance, heapq_node.cur_point, heapq_node.pre_point
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
                add_data = HeapQNode(distance, (new_node_x, new_node_y), cur_point)
                self.append_to_list(new_node_list, add_data)
        return dp[-1][-1]


solution = Solution()
data = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(solution.minimumEffortPath(data))
