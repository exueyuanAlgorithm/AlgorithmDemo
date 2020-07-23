class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
