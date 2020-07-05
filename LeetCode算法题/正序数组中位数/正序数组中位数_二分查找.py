import math
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        print("nums1为:{},nums2为:{}".format(nums1, nums2))
        allLen = len(nums1) + len(nums2)
        isDoubleMiddle = allLen % 2 == 0
        middleNumPosition = allLen // 2
        if isDoubleMiddle:
            if nums1 and not nums2:
                return (nums1[middleNumPosition-1] + nums1[middleNumPosition])/2
            elif not nums1 and nums2:
                return (nums2[middleNumPosition-1] + nums2[middleNumPosition])/2

            if allLen == 2:
                nums1.extend(nums2)
                return (nums1[0]+nums1[1])/2
            leftNum = min(len(nums1), len(nums2), middleNumPosition // 2)
        else:
            if nums1 and not nums2:
                return nums1[middleNumPosition]
            elif not nums1 and nums2:
                return nums2[middleNumPosition]
            if allLen == 1:
                nums1.extend(nums2)
                return nums1[0]
            leftNum = min(len(nums1), len(nums2), math.ceil(middleNumPosition / 2))
        print(leftNum)
        nums1_max = nums1[leftNum - 1]
        nums1_min = nums1[-leftNum]
        nums2_max = nums2[leftNum - 1]
        nums2_min = nums2[-leftNum]
        print("最大值:", nums1_max, nums2_max)
        print("最小值:", nums1_min, nums2_min)
        # 进行 nums1_max 和 nums2_max的比较
        if nums1_max >= nums2_max:
            nums1_left_delete = False
        else:
            nums1_left_delete = True

        if nums1_min <= nums2_min:
            nums1_right_delete = False
        else:
            nums1_right_delete = True

        if nums1_left_delete and nums1_right_delete:
            if leftNum * 2 >= len(nums1):
                nums1 = []
            else:
                nums1 = nums1[leftNum:-leftNum]
        elif not nums1_left_delete and not nums1_right_delete:
            if leftNum * 2 >= len(nums2):
                nums2 = []
            else:
                nums2 = nums2[leftNum:-leftNum]
        elif nums1_left_delete and not nums1_right_delete:
            if leftNum >= len(nums1):
                nums1 = []
            else:
                nums1 = nums1[leftNum:]

            if leftNum >= len(nums2):
                nums2 = []
            else:
                nums2 = nums2[:-leftNum]
        elif not nums1_left_delete and nums1_right_delete:
            if leftNum >= len(nums1):
                nums1 = []
            else:
                nums1 = nums1[:-leftNum]

            if leftNum >= len(nums2):
                nums2 = []
            else:
                nums2 = nums2[leftNum:]
        return self.findMedianSortedArrays(nums1, nums2)








solution = Solution()
print(solution.findMedianSortedArrays([1], [2,3,4,5,6,7, 8]))
