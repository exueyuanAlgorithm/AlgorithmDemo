class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        answer_dict = {}
        for answer in answers:
            answer_dict[answer] = answer_dict.get(answer, 0) + 1
        tuzi_sum = 0
        for key, value in answer_dict.items():
            shang = value // (key+1)
            if value % (key+1) > 0:
                shang += 1
            tuzi_sum = tuzi_sum + (key+1)*shang
        return tuzi_sum


solution = Solution()
print(solution.numRabbits([2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1]))
