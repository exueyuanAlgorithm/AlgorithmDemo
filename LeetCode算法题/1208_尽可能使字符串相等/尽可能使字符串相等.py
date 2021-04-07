import bisect
from itertools import accumulate


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        cost_list = [abs(ord(item1) - ord(item2)) for item1, item2 in zip(s, t)]
        print(cost_list)
        i = 0
        j = 0
        max_num = 0
        already_cost = 0
        while True:
            if j >= len(t):
                break
            already_cost += cost_list[j]
            if already_cost <= maxCost:
                changdu = j - i + 1
                if changdu > max_num:
                    max_num = changdu
                j += 1
            else:
                j += 1
                already_cost -= cost_list[i]
                i += 1

        return max_num


# class Solution2(object):
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
#         maxLength = 0
#
#         for i in range(1, n + 1):
#             start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
#             maxLength = max(maxLength, i - start)
#
#         return maxLength
# solution2 = Solution2()
# print(solution2.equalSubstring("krrgw", "zjxss", 19))

solution = Solution()
print(solution.equalSubstring("krrgw", "zjxss", 19))