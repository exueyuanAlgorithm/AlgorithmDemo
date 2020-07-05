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
            needDeleteHalfNum = middleNumPosition // 2
        else:
            if nums1 and not nums2:
                return nums1[middleNumPosition]
            elif not nums1 and nums2:
                return nums2[middleNumPosition]
            if allLen == 1:
                nums1.extend(nums2)
                return nums1[0]
            needDeleteHalfNum = math.ceil(middleNumPosition / 2)

        print(needDeleteHalfNum)
        if needDeleteHalfNum <= len(nums1):
            nums1_max = nums1[needDeleteHalfNum - 1]
            nums1_min = nums1[-needDeleteHalfNum]
        else:
            nums1_max = nums1[-1]
            nums1_min = nums1[0]
        if needDeleteHalfNum <= len(nums2):
            nums2_max = nums2[needDeleteHalfNum - 1]
            nums2_min = nums2[-needDeleteHalfNum]
        else:
            nums2_max = nums2[-1]
            nums2_min = nums2[0]
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
            if needDeleteHalfNum * 2 >= len(nums1):
                nums1 = []
            else:
                nums1 = nums1[needDeleteHalfNum:-needDeleteHalfNum]
        elif not nums1_left_delete and not nums1_right_delete:
            if needDeleteHalfNum * 2 >= len(nums2):
                nums2 = []
            else:
                nums2 = nums2[needDeleteHalfNum:-needDeleteHalfNum]
        elif nums1_left_delete and not nums1_right_delete:
            if needDeleteHalfNum >= len(nums1):
                cha = needDeleteHalfNum - len(nums1)
                nums2 = nums2[cha:]
                nums1 = []
            else:
                nums1 = nums1[needDeleteHalfNum:]

            if needDeleteHalfNum >= len(nums2):
                cha = needDeleteHalfNum - len(nums2)
                nums1 = nums1[:len(nums1)-cha]
                nums2 = []
            else:
                nums2 = nums2[:-needDeleteHalfNum]
        elif not nums1_left_delete and nums1_right_delete:
            if needDeleteHalfNum >= len(nums1):
                cha = needDeleteHalfNum - len(nums1)
                nums2 = nums2[:len(nums2)-cha]
                nums1 = []
            else:
                nums1 = nums1[:-needDeleteHalfNum]

            if needDeleteHalfNum >= len(nums2):
                cha = needDeleteHalfNum - len(nums2)
                nums1 = nums1[cha:]
                nums2 = []
            else:
                nums2 = nums2[needDeleteHalfNum:]
        return self.findMedianSortedArrays(nums1, nums2)








solution = Solution()
print(solution.findMedianSortedArrays([3], [-2, -1]))
