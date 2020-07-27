class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        s_position = 0
        t_position = 0

        while s_position < len(s):
            s_item = s[s_position]
            isFind = False
            while t_position < len(t):
                t_item = t[t_position]
                t_position += 1
                if s_item == t_item:
                    isFind = True
                    s_position += 1
                    break
            if not isFind:
                return False
        return True

solution = Solution()
print(solution.isSubsequence("axc", "ahbgdc"))