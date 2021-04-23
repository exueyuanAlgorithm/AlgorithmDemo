
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        result_list = []
        for i in range(1, z+1):
            for j in range(1, z+1):
                if customfunction.f(i, j) == z:
                    result_list.append([i, j])
        return result_list