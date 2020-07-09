class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ""
        for i in range(len(s)-1, -1, -1):
            if s[:i] == s[len(s)-i:]:
                return s[:i]
        return ""

solution = Solution()
print(solution.longestPrefix("ababab"))