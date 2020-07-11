class Solution(object):
    def sortNums(self, nums, i, j):
        if i >= j:
            return
        min = i
        max = j
        while i < j:
            while i < j and nums[i] <= nums[j]:
                j -= 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

            while i < j and nums[i] <= nums[j]:
                i += 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        else:
            self.sortNums(nums, min, i-1)
            self.sortNums(nums, i+1, max)

    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0

        self.sortNums(nums, 0, len(nums)-1)
        minDiff = 99999999999999
        for i in range(4):
            rightQie = 3-i
            if rightQie == 0:
                newNums = nums[i:]
            else:
                newNums = nums[i:-rightQie]
            if newNums[-1]-newNums[0] < minDiff:
                minDiff = newNums[-1]-newNums[0]
        return minDiff





solution = Solution()
print(solution.minDifference([5,3,2,4]))
