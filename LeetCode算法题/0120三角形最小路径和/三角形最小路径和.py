class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i, rowArray in enumerate(triangle):
            if i > 0:
                preRowArray = triangle[i-1]
                for j, num in enumerate(rowArray):
                    if j == 0:
                        rowArray[j] = preRowArray[0] + num
                    elif j == len(rowArray)-1:
                        rowArray[j] = preRowArray[-1] + num
                    else:
                        rowArray[j] = min((preRowArray[j - 1] + num), (preRowArray[j] + num))
        return min(triangle[-1])


solution = Solution()
print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
