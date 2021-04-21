class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        xiabiao_list = [i for i in range(len(nums2))]
        xiabiao_list_list = [xiabiao_list]
        result_list = []
        while True:
            min_xiabiao = None
            min_sum = 9999999999999999
            for position1, xiabiao_list in enumerate(xiabiao_list_list):
                position2 = -1
                if xiabiao_list:
                    position2 = xiabiao_list[0]
                if position1 < len(nums1) and 0 <= position2 < len(nums2):
                    temp_sum = nums1[position1] + nums2[position2]
                    if temp_sum < min_sum:
                        min_sum = temp_sum
                        min_xiabiao = (position1, position2)
            if min_xiabiao:
                result_list.append([nums1[min_xiabiao[0]], nums2[min_xiabiao[1]]])
                if len(result_list) == k:
                    return result_list
                num = xiabiao_list_list[min_xiabiao[0]].pop(0)
                if min_xiabiao[0] + 1 < len(xiabiao_list_list):
                    xiabiao_list_list[min_xiabiao[0] + 1].append(num)
                else:
                    xiabiao_list_list.append([num])
            else:
                break
        return result_list

solution = Solution()
print(solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 3))