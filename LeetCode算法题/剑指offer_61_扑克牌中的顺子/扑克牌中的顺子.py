class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        zero_num = 0
        nums.sort()
        last_num = 15
        for position, num in enumerate(nums):
            if num == 0:
                zero_num += 1
            else:
                if last_num > 13:
                    last_num = num
                else:
                    if num == last_num:
                        return False
                    if num == last_num + 1:
                        last_num = num
                    else:
                        zero_num -= num - last_num - 1
                        if zero_num < 0:
                            return False
                        last_num = num
        return True

solution = Solution()
print(solution.isStraight([9, 0, 6, 0, 10]))