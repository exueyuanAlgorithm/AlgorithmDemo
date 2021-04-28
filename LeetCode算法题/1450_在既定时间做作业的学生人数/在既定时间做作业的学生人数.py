class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        num_ = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                num_ += 1
        return num_