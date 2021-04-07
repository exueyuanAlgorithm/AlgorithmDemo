class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        result_set = set()
        for item3 in self.generateParenthesis(n-1):
            result3 = "(" + item3 + ")"
            result_set.add(result3)
        for i in range(1, n):
            for item1 in self.generateParenthesis(i):
                for item2 in self.generateParenthesis(n - i):
                    result_2 = item1 + item2
                    result_set.add(result_2)
        return list(result_set)

solution = Solution()
print(solution.generateParenthesis(1))