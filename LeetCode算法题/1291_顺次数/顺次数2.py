class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        nums = [12, 23, 34, 45, 56, 67, 78, 89,
                123, 234, 345, 456, 567, 678, 789,
                1234, 2345, 3456, 4567, 5678, 6789,
                12345, 23456, 34567, 45678, 56789,
                123456, 234567, 345678, 456789,
                1234567, 2345678, 3456789,
                12345678, 23456789,
                123456789]
        result_list = []
        low_position = -1
        for position, num in enumerate(nums):
            if num >= low:
                low_position = position
                break
        if low_position < 0:
            return result_list
        high_position = -1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num <= high:
                high_position = i
                break
        if high_position < 0:
            return result_list
        if low_position > high_position:
            return result_list
        return nums[low_position:high_position+1]


