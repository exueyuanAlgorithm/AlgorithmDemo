class Solution:
    def gongyueshu(self, a, b):
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return a

    def checkTwoNum(self, leftNum, rightNum):
        if leftNum == rightNum:
            return True
        if self.gongyueshu(leftNum, rightNum) > 1:
            return True
        else:
            return False

    def splitArray(self, nums: list) -> int:
        dp = [-1]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            numI = nums[i]
            dp[i] = dp[i-1] + 1
            for j in range(i):
                numJ = nums[j]
                if self.checkTwoNum(numJ, numI):
                    if j == 0:
                        dp[i] = 1
                    else:
                        if dp[j-1] + 1 < dp[i]:
                            dp[i] = dp[j-1] + 1
        return dp[-1]



solution = Solution()
print(solution.splitArray([2,3,5,7]))