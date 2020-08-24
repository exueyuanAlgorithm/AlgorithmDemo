class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        haoshuduiCount = 0
        i = 0
        while i < len(nums) - 1:
            num1 = nums[i]
            j = i + 1
            while j < len(nums):
                num2 = nums[j]
                if num1 == num2:
                    haoshuduiCount += 1
                j += 1
            i += 1
        return haoshuduiCount