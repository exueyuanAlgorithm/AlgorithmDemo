class Solution:
    def findItemPositionNotStar(self, s: str, findStr: str) -> int:
        if len(s) < len(findStr):
            return -1
        for s_position in range(len(s)-len(findStr)+1):
            if self.isMatchNotStar(s[s_position:s_position+len(findStr)], findStr):
                return s_position
        return -1

    def findItemPositionNotStarR(self, s: str, findStr: str) -> int:
        if len(s) < len(findStr):
            return -1
        for s_position in range(len(s)-len(findStr)+1, -1, -1):
            if self.isMatchNotStar(s[s_position:s_position+len(findStr)], findStr):
                return s_position
        return -1

    def isMatchNotStar(self, s: str, p: str) -> bool:
        """
        这个里面是没有*的
        :param s:
        :param p:
        :return:
        """
        s_position = 0
        p_position = 0
        while p_position < len(p):
            p_item = p[p_position]
            if p_item == "?":
                if len(s) <= s_position:
                    return False
                s_position += 1
                p_position += 1
            else:
                if len(s) <= s_position:
                    return False
                if s[s_position] == p_item:
                    s_position += 1
                else:
                    return False
                p_position += 1
        if s_position < len(s):
            return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        if "*" not in p:
            return self.isMatchNotStar(s, p)

        p_array = list(filter(None, p.split("*")))
        if p_array:
            if p[0] != "*":
                index = self.findItemPositionNotStar(s, p_array[0])
                if index != 0:
                    return False
            if p[-1] != "*":
                index = self.findItemPositionNotStarR(s, p_array[-1])
                if index != len(s) - len(p_array[-1]):
                    return False

        for p_item in p_array:
            index = self.findItemPositionNotStar(s, p_item)
            if index == -1:
                return False
            else:
                s = s[index + len(p_item):]
        return True



s = "acdcb"
p = "a*cb"
s = "mississippi"
p = "m??*ss*?i*pi"
solution = Solution()
# print(solution.findItemPositionNotStar("abbbssadk", "b??s"))
print(solution.isMatch(s, p))
