class Solution:
    def startHandleP(self, p:str):
        new_p = ""
        last_item = ""
        for item in p:
            if not (item == "*" and item == last_item):
                new_p += item
            last_item = item
        return new_p

    def isMatch(self, s: str, p: str) -> bool:
        # 这一步多个*融合成一个*
        p = self.startHandleP(p)
        print(p)
        s_position = 0
        p_position = 0
        while p_position < len(p):
            p_item = p[p_position]
            if p_item == "?":
                if len(s) <= s_position:
                    return False
                s_position += 1
                p_position += 1
            elif p_item == "*":
                p_position += 1
                while True:
                    if len(s) < s_position:
                        return False
                    new_p = p[p_position:]
                    new_s = s[s_position:]
                    isMatch = self.isMatch(new_s, new_p)
                    if isMatch:
                        return True
                    s_position += 1
                pass
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




solution = Solution()
print(solution.isMatch("acdcb", "a********"))