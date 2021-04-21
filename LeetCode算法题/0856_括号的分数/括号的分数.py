class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        all_fenshu = 0
        for item in S:
            if item == "(":
                stack.append([item, 0])
            if item == ")":
                pop_item = stack.pop()
                fenshu = pop_item[1] * 2 if pop_item[1] != 0 else 1
                if stack:
                    stack[-1][1] += fenshu
                else:
                    all_fenshu += fenshu
        return all_fenshu
solution = Solution()
print(solution.scoreOfParentheses("()"))
