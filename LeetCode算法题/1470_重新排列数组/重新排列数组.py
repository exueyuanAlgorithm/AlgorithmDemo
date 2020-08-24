class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        returnList = []
        for i in range(n):
            returnList.append(nums[i])
            returnList.append(nums[i + n])
        return returnList
