from data import data


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        dp = [[0] * n for _ in range(m)]
        fangxiang_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bianli_list = [(0, 0)]
        already_node_set = set()
        already_node_set.add((0, 0))
        while True:
            i = 0
            min_pre_node = None
            min_new_node = None
            min_distance = 999999999999
            while i < len(bianli_list):
                node = bianli_list[i]
                has_next_node = False
                for fangxiang in fangxiang_list:
                    new_node_x = node[0] + fangxiang[0]
                    new_node_y = node[1] + fangxiang[1]
                    if new_node_x < 0 or new_node_y < 0 or new_node_x >= m or new_node_y >= n:
                        continue
                    if (new_node_x, new_node_y) in already_node_set:
                        continue
                    has_next_node = True
                    distance = abs(heights[new_node_x][new_node_y] - heights[node[0]][node[1]])
                    if distance < min_distance:
                        min_distance = distance
                        min_new_node = (new_node_x, new_node_y)
                        min_pre_node = node
                if has_next_node:
                    i += 1
                else:
                    bianli_list.remove(node)
            if min_new_node is None:
                break
            else:
                dp[min_new_node[0]][min_new_node[1]] = max(dp[min_pre_node[0]][min_pre_node[1]], min_distance)
                already_node_set.add(min_new_node)
                bianli_list.append(min_new_node)
                if min_new_node[0] == len(heights) - 1 and min_new_node[1] == len(heights[0]) - 1:
                    break
        return dp[-1][-1]


solution = Solution()
print(solution.minimumEffortPath(data))
