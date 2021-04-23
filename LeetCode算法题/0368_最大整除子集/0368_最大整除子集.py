class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_position = 0
        max_size = -1
        max_num = -1
        for position, dp_num in enumerate(dp):
            if dp_num > max_size:
                max_size = dp_num
                max_position = position
                max_num = nums[position]
        result_list = []
        for i in range(max_position, -1, -1):
            if i == max_position:
                result_list.append(max_num)
                max_size -= 1
            elif dp[i] == max_size and max_num % nums[i] == 0:
                result_list.append(nums[i])
                max_size -= 1
                max_num = nums[i]
            if max_size == 0:
                break
        return result_list

solution = Solution()
print(solution.largestDivisibleSubset([3, 4, 6, 8, 12, 16, 32]))
