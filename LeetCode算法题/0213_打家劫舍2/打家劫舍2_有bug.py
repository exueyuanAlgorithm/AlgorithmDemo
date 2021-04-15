class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        sum_0 = 0
        sum_1 = 0
        for position, num in enumerate(nums):
            if position % 2 == 0:
                sum_0 += num
            else:
                sum_1 += num
        if len_nums % 2 == 0:
            return max(sum_0, sum_1)
        else:
            return max(sum_1, sum_0 - nums[0], sum_0 - nums[-1])


solution = Solution()
print(solution.rob([2, 3, 2]))
