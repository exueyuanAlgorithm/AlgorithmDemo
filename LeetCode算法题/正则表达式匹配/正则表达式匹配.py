class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_position = 0
        p_position = 0
        while p_position < len(p):
            p_item = p[p_position]
            p_item_next = None
            if p_position+1 < len(p):
                p_item_next = p[p_position+1]

            if p_item == ".":
                if p_item_next == "*":
                    p_position += 2
                    while True:
                        if len(s) < s_position:
                            return False
                        new_s = s[s_position:]
                        new_p = p[p_position:]
                        isMatch = self.isMatch(new_s, new_p)
                        if isMatch:
                            return True
                        s_position += 1
                else:
                    if len(s) <= s_position:
                        return False
                    s_position += 1
                    p_position += 1
            else:
                if p_item_next == "*":
                    p_position += 2
                    while True:
                        new_s = s[s_position:]
                        new_p = p[p_position:]
                        isMatch = self.isMatch(new_s, new_p)
                        if isMatch:
                            return True
                        if len(s) <= s_position:
                            return False
                        if s[s_position] == p_item:
                            s_position += 1
                        else:
                            break
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
print(solution.isMatch("a", "ab*a"))