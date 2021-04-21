class Solution(object):

    def numDecodings(self, s):
        if s.startswith("0"):
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i, item in enumerate(s):
            if i == 0:
                dp[1] = 1
                continue
            else:
                qingkuang1 = 0
                if item != "0":
                    qingkuang1 = dp[i]
                qingkuang2 = 0
                new_s = s[i - 1:i + 1]
                if 1 <= int(new_s) <= 26 and s[i - 1] != "0":
                    qingkuang2 = dp[i - 1]
                dp[i + 1] = qingkuang1 + qingkuang2
        return dp[-1]


solution = Solution()
print(solution.numDecodings("2101"))
