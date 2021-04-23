class Solution(object):
    def findSolution(self, customfunction, z):
        ans, x, y = [], 1, z
        while x <= z and y >= 1:
            res = customfunction.f(x, y)
            if res < z:
                x += 1
            elif res > z:
                y -= 1
            if res == z:
                ans.append([x, y])
                x += 1
                y -= 1
        return ans
