class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        position = m + n - 1
        while True:
            if position < 0:
                return
            if j < 0:
                return
            if i < 0:
                nums1[position] = nums2[j]
                j -= 1
                position -= 1
            elif nums1[i] <= nums2[j]:
                nums1[position] = nums2[j]
                j -= 1
                position -= 1
            else:
                nums1[position] = nums1[i]
                i -= 1
                position -= 1



solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1, m = 3, nums2=[2, 5, 6], n = 3)
print(nums1)
