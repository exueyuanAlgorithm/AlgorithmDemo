class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        sum_ = 0
        for i in range(0, len(time)-1):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    sum_ += 1
        return sum_