class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, min(i + k + 1, length)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
