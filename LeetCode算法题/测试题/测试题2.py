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

    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sumList = []
        for i in range(n):
            sumList.append(nums[i])
            for j in range(i+1, n):
                sumList.append(sumList[-1]+nums[j])
        print(sumList)
        self.sortNums(sumList, 0, len(sumList)-1)
        print(sumList)
        returnSum = 0
        for i in range(left-1, right):
            returnSum += sumList[i]
        return returnSum % (10**9+7)




solution = Solution()
print(solution.rangeSum([1, 2, 3, 4], 4, 1, 10))
