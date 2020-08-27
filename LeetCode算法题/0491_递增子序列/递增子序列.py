class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        xuhaoList = []
        keyDict = {}
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                print(nums[i], nums[j])
                if nums[i] <= nums[j]:
                    xuhaoList.append([i, j])
                    keyDict[i] = j
                j += 1
            i += 1
        for xuhaoDui in xuhaoList:
            if xuhaoDui[-1] in keyDict:
                keyDict[xuhaoDui[-1]]
        print(xuhaoList)
        print(keyDict)


solution = Solution()
print(solution.findSubsequences([8, 4, 7, 9, 7]))


print()