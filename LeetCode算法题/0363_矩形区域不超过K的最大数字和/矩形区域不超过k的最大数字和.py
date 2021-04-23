class Solution(object):
    def maxSumSubmatrix(self, matrix, data):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)] for _ in range(m)]
        max_num = -999999999999
        for i in range(m):
            for j in range(i, m):
                for k in range(n):
                    for s in range(k, n):
                        if i == j and k == s:
                            dp[i][j][k][s] = matrix[i][k]
                        elif i == j:
                            dp[i][j][k][s] = matrix[i][s] + dp[i][j][k][s - 1]
                        elif k == s:
                            dp[i][j][k][s] = matrix[j][s] + dp[i][j - 1][k][s]
                        else:
                            dp[i][j][k][s] = dp[i][j - 1][k][s] + dp[i][j][k][s - 1] + matrix[j][s] - dp[i][j - 1][k][s - 1]
                        bijiao_num = dp[i][j][k][s]
                        if bijiao_num == data:
                            return data
                        if max_num < bijiao_num <= data:
                            max_num = bijiao_num
        return max_num

