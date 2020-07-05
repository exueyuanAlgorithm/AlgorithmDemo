

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == x or z == y or z == x + y:
            return True
        maxXY = max(x, y)
        minXY = min(x, y)
        if minXY == 0:
            if z == 0 or z == maxXY:
                return True
            else:
                return False
        cao = 0
        while True:
            if cao == z:
                return True
            cao += minXY
            if cao == z:
                return True
            if cao > maxXY:
                cao = cao % maxXY
            elif cao == maxXY:
                return False


s = Solution()
print(s.canMeasureWater(0, 2, 1))
