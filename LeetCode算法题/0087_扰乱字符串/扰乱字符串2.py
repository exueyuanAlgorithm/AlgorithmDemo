class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        dp = [[[False for _ in range(length + 1)] for _ in range(length)] for _ in range(length)]
        for position1, item_1 in enumerate(s1):
            for position2, item_2 in enumerate(s2):
                dp[position1][position2][1] = item_1 == item_2
        for len2 in range(2, length + 1):
            for i in range(length -len2 + 1):
                for j in range(length - len2 + 1):
                    for k in range(1, len2):
                        if dp[i][j][k] and dp[i+k][j+k][len2-k]:
                            dp[i][j][len2] = True
                            break
                        if dp[i][j+len2-k][k] and dp[i+k][j][len2-k]:
                            dp[i][j][len2] = True
                            break

        return dp[0][0][length]



solution = Solution()
x1 = "eebaacbcbcadaaedceaaacadccd"
x2 = "eadcaacabaddaceacbceaabeccd"
print(solution.isScramble(x1, x2))
