class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_insert_low_high(nums, target, low, high):
            if low > high:
                return low
            elif low == high and nums[low] == target:
                return low
            elif low == high and nums[low] < target:
                return low + 1
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                return search_insert_low_high(nums, target, low, middle - 1)
            else:
                return search_insert_low_high(nums, target, middle + 1, high)

        low = 0
        high = len(nums) - 1
        return search_insert_low_high(nums, target, low, high)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 0))
