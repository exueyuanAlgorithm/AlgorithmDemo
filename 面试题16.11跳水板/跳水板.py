class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        mubanList = []
        for i in range(k + 1):
            reAdd = i *longer + (k-i)* shorter
            if mubanList:
                if mubanList[-1] != reAdd:
                    mubanList.append(reAdd)
            else:
                mubanList.append(reAdd)
        return mubanList
