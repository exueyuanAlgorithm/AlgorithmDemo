class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack_list = []
        for item in tokens:
            if "0" <= item <= "9" or len(item) > 1:
                stack_list.append(int(item))
            elif item == "+":
                result = stack_list[-2] + stack_list[-1]
                stack_list.pop()
                stack_list.pop()
                stack_list.append(result)
            elif item == "-":
                result = stack_list[-2] - stack_list[-1]
                stack_list.pop()
                stack_list.pop()
                stack_list.append(result)
            elif item == "*":
                result = stack_list[-2] * stack_list[-1]
                stack_list.pop()
                stack_list.pop()
                stack_list.append(result)
            elif item == "/":
                result = int(stack_list[-2] / stack_list[-1])
                stack_list.pop()
                stack_list.pop()
                stack_list.append(result)
        return int(round(stack_list[0]))


solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
