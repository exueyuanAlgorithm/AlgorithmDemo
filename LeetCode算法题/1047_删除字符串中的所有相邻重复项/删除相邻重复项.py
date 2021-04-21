class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        while i < len(S) - 1:
            if S[i] == S[i + 1]:
                S = S[:i] + S[i + 2:]
                i -= 1
                if i < 0:
                    i = 0
                continue
            i += 1
        return S

solution = Solution()
print(solution.removeDuplicates("abbaca"))

