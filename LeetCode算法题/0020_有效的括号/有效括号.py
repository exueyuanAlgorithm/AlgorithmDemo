class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if item in "({[":
                stack.append(item)
            elif item == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif item == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif item == "]":
                if not stack or stack.pop() != "[":
                    return False
        if stack:
            return False
        return True
