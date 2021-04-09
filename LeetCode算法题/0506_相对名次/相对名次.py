class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_2 = [(position, item) for position, item in enumerate(score)]
        score_2.sort(key=lambda item: item[1], reverse=True)
        result_list = [""] * len(score)
        for position, score_tuple in enumerate(score_2):
            if position == 0:
                result_list[score_tuple[0]] = "Gold Medal"
            elif position == 1:
                result_list[score_tuple[0]] = "Silver Medal"
            elif position == 2:
                result_list[score_tuple[0]] = "Bronze Medal"
            else:
                result_list[score_tuple[0]] = str(position+1)
        return result_list

solution = Solution()
print(solution.findRelativeRanks([1,3,7,8 ,9,10]))