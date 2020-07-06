# coding=utf-8
def getLoopNums(num):
    startNum = 1
    yushuList = []
    while True:
        # print("开始的数字为:{},余数list为:{}".format(startNum, yushuList))
        while startNum < num:
            startNum = startNum * 10
        if startNum % num == 0:
            return -1
        else:
            yushu = startNum % num
            if yushu not in yushuList:
                yushuList.append(yushu)
                startNum = startNum % num
            else:
                index = yushuList.index(yushu)
                return len(yushuList[index:])


maxLoopNum = -1
maxLoopNumI = 0
for i in range(2, 1001):
    loopNum = getLoopNums(i)
    if loopNum > maxLoopNum:
        maxLoopNum = loopNum
        maxLoopNumI = i
print(maxLoopNumI, maxLoopNum)
