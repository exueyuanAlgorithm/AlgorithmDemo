class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for position,num in enumerate(nums):
            if nums[position-1] >= nums[position]:
                return nums[position]