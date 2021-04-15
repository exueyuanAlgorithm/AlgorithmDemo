import copy


class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.num = 0
        self.num_list = []
        self.sort_num_list = None
        self.k = k
        self.m = m

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.num_list) < self.m:
            self.num_list.append(num)
        else:
            self.num_list.pop(0)
            self.num_list.append(num)
        if len(self.num_list) == self.m:
            self.sort_num_list = copy.deepcopy(self.num_list)
            self.sort_num_list.sort()

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.num_list) < self.m:
            return -1
        return sum(self.sort_num_list[self.k:-self.k]) // (self.m - 2 * self.k)
