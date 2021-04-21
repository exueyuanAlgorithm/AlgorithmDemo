class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        result_list = []
        while True:
            num1 = nums1[i]
            num2 = nums2[j]
            result_list.append([num1, num2])
            if len(result_list) >= k:
                break
            sum1 = 999999999999999
            sum2 = 999999999999999
            if i+1 >= len(nums1) and j+1 >= len(nums2):
                break
            if i+1 < len(nums1):
                next_num1 = nums1[i+1]
                sum1 = next_num1 + num2
            if j+1 < len(nums2):
                next_num2 = nums2[j+1]
                sum2 = next_num2 + num1
            if sum1 > sum2:
                j += 1
            else:
                i += 1
        return result_list

solution = Solution()
print(solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 10))



