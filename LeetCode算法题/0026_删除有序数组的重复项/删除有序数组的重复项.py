class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        delete_num = 0
        for i, num in enumerate(nums):
            if i - 1 >= 0 and num == nums[i - 1]:
                delete_num += 1
            else:
                nums[j] = num
                j += 1
        return len(nums) - delete_num
