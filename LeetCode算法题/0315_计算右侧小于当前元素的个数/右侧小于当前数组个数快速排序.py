class Solution(object):
    def sortNums(self, nums, i, j):
        if i >= j:
            return
        min = i
        max = j
        while i < j:
            while i < j and nums[i] >= nums[j]:
                j -= 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

            while i < j and nums[i] >= nums[j]:
                i += 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        else:
            self.sortNums(nums, min, i-1)
            self.sortNums(nums, i+1, max)




    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        for i in range(len(nums)):
            newNums = nums[i:]
            i = 0
            j = len(newNums)-1
            self.sortNums(newNums, i, j)
            print(newNums)


solution = Solution()
print(solution.countSmaller([5, 2, 6, 1]))