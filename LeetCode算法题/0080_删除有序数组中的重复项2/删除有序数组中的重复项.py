class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        while True:
            if i >= len(nums) - 2:
                break
            current_num = nums[i]
            next_num = nums[i + 1]
            next_next_num = nums[i + 2]
            if current_num == next_num == next_next_num:
                # 删除 next_next_num,并且
                nums.pop(i + 2)
                continue
            else:
                i += 1
        return len(nums)


solution = Solution()
nums = [0,0,1,1,1,1,2,3,3]
length = solution.removeDuplicates(nums)
print(length, nums)
