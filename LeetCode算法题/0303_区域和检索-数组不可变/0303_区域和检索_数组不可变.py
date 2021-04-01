class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_list = []
        for i, num in enumerate(nums):
            if i == 0:
                self.sum_list.append(num)
            else:
                self.sum_list.append(self.sum_list[i - 1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.sum_list[right]
        return self.sum_list[right] - self.sum_list[left - 1]
