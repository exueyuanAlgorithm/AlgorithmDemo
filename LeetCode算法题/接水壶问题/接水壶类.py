import sys
sys.setrecursionlimit(1000000)

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        alreadyHaveWaterList = []
        x_have = 0
        y_have = 0
        alreadyHaveWaterList.append((x_have, y_have))
        self.pullWater(x, y, x_have, y_have, alreadyHaveWaterList)
        print("目前的状况:{}".format(alreadyHaveWaterList))
        for alreadyHaveWater in alreadyHaveWaterList:
            if alreadyHaveWater[0] == z or alreadyHaveWater[1] == z or alreadyHaveWater[0] + alreadyHaveWater[1] == z:
                return True
        return False

    def pullWater(self, x, y, x_have, y_have, alreadyHaveWaterList):
        print("已经存在的warterList:{}".format(alreadyHaveWaterList))
        print("*"*1000)
        # 左清空
        if x_have > 0:
            x_have_new = 0
            if not self.checkIfHaveWater(alreadyHaveWaterList, x_have_new, y_have):
                alreadyHaveWaterList.append((x_have_new, y_have))
                self.pullWater(x, y, x_have_new, y_have, alreadyHaveWaterList)
        # 右清空
        if y_have > 0:
            y_have_new = 0
            if not self.checkIfHaveWater(alreadyHaveWaterList, x_have, y_have_new):
                alreadyHaveWaterList.append((x_have, y_have_new))
                self.pullWater(x, y, x_have, y_have_new, alreadyHaveWaterList)
        # 左加满
        if x_have < x:
            x_have_new = x
            if not self.checkIfHaveWater(alreadyHaveWaterList, x_have_new, y_have):
                alreadyHaveWaterList.append((x_have_new, y_have))
                self.pullWater(x, y, x_have_new, y_have, alreadyHaveWaterList)
        # 右加满
        if y_have < y:
            y_have_new = y
            if not self.checkIfHaveWater(alreadyHaveWaterList, x_have, y_have_new):
                alreadyHaveWaterList.append((x_have, y_have_new))
                self.pullWater(x, y, x_have, y_have_new, alreadyHaveWaterList)
        # 左倒右
        x_have_new, y_have_new = self.pull(x, y, x_have, y_have)
        if not self.checkIfHaveWater(alreadyHaveWaterList, x_have_new, y_have_new):
            alreadyHaveWaterList.append((x_have_new, y_have_new))
            self.pullWater(x, y, x_have_new, y_have_new, alreadyHaveWaterList)
        # 右倒左
        y_have_new, x_have_new = self.pull(y, x, y_have, x_have)
        if not self.checkIfHaveWater(alreadyHaveWaterList, x_have_new, y_have_new):
            alreadyHaveWaterList.append((x_have_new, y_have_new))
            self.pullWater(x, y, x_have_new, y_have_new, alreadyHaveWaterList)

    def checkIfHaveWater(self, alreadyHaveWaterList, x_have, y_have):
        for alreadyhaveWater in alreadyHaveWaterList:
            if alreadyhaveWater[0] == x_have and alreadyhaveWater[1] == y_have:
                return True
        return False

    # 从x倒向y
    def pull(self, x, y, x_have, y_have):
        # 检测x倒空，还是y倒满
        if y_have + x_have > y:
            # y倒满
            return x_have - (y - y_have), y
        else:
            # x倒空
            return 0, y_have + x_have


s = Solution()
print(s.canMeasureWater(22003, 31237, 1))
