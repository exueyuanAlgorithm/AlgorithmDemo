class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        time_dict = {}
        for item in time:
            quyu = item % 60
            time_dict[quyu] = time_dict.get(quyu, 0) + 1
        all_num = 0
        for key, value in time_dict.items():
            if 0 < key < 30:
                all_num += time_dict.get(60 - key, 0) * value
        zero_num = time_dict.get(0, 0)
        thirty_num = time_dict.get(30, 0)
        all_num += zero_num * (zero_num - 1) // 2
        all_num += thirty_num * (thirty_num - 1) // 2
        return all_num


solution = Solution()
print(solution.numPairsDivisibleBy60([60, 60, 60]))
