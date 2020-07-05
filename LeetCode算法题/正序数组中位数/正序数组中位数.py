class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        allLen = len(nums1) + len(nums2)
        isDoubleMiddle = allLen % 2 == 0
        middleNumPosition = allLen // 2

        sortList = []
        while True:
            if nums1 and nums2:
                nums1_num = nums1[0]
                nums2_num = nums2[0]
                if nums1_num <= nums2_num:
                    sortList.append(nums1.pop(0))
                else:
                    sortList.append(nums2.pop(0))
            else:
                print("此时的sortList:{}".format(sortList))
                if not nums1:
                    sortList.extend(nums2)
                if not nums2:
                    sortList.extend(nums1)
                if isDoubleMiddle:
                    return (sortList[middleNumPosition] + sortList[middleNumPosition-1]) / 2
                else:
                    return sortList[middleNumPosition]
            print("此时的sortList:{}".format(sortList))
            if isDoubleMiddle:
                if len(sortList) == middleNumPosition + 1:
                    return (sortList[-2] + sortList[-1]) / 2
            else:
                if len(sortList) == middleNumPosition + 1:
                    return sortList[-1]


solution = Solution()
print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]))
