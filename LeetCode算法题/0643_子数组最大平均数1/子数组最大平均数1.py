class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        max_sum = -1000000000000
        last_sum = None
        for position in range(0, length-k +1):
            if position == 0:
                last_sum = sum(nums[position:position+k])
                max_sum = max(max_sum, last_sum)
            else:
                last_sum -= nums[position - 1]
                last_sum += nums[position + k - 1]
                max_sum = max(max_sum, last_sum)
        return max_sum / k

solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
