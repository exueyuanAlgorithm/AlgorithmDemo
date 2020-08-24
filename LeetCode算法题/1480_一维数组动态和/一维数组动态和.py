class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        sumList = [0] * len(nums)
        sumList[0] = nums[0]
        for position, num in enumerate(nums):
            if position > 0:
                sumList[position] = sumList[position-1] + nums[position]
        print(sumList)
        return sumList

solution = Solution()
print(solution.runningSum([2,3,5]))