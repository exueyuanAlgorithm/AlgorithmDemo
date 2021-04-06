def trap(height: list)->int:
    rainPositionStack = []
    rainTupleList = []
    for num, currentHeight in enumerate(height):
        print("第{}轮，高度为:{}".format(num, rainPositionStack))
        if currentHeight > 0:
            for lastPosition in reversed(rainPositionStack):
                position = rainPositionStack[-1]
                if height[lastPosition] <= currentHeight:
                    rainPositionStack.pop()
                for rainTuple in reversed(rainTupleList):
                    if rainTuple[0] >= position and rainTuple[1] <= num:
                        rainTupleList.pop()
                    else:
                        break
                rainTupleList.append((position, num))
            rainPositionStack.append(num)
    print("{},最后的tuple:{}".format(rainPositionStack, rainTupleList))
    allRain = 0
    for rainTuple in rainTupleList:
        leftHeight = rainTuple[0]
        rightHeight = rainTuple[1]
        minHeight = min(height[leftHeight], height[rightHeight])
        for i in range(leftHeight + 1, rightHeight):
            currentHeight = height[i]
            currentRain = minHeight - currentHeight
            allRain += currentRain
    return allRain

class Solution(object):
    def trap(self, height):
        rainPositionStack = []
        rainTupleList = []
        for num, currentHeight in enumerate(height):
            print("第{}轮，高度为:{}".format(num, rainPositionStack))
            if currentHeight > 0:
                for lastPosition in reversed(rainPositionStack):
                    position = rainPositionStack[-1]
                    if height[lastPosition] <= currentHeight:
                        rainPositionStack.pop()
                    for rainTuple in reversed(rainTupleList):
                        if rainTuple[0] >= position and rainTuple[1] <= num:
                            rainTupleList.pop()
                        else:
                            break
                    rainTupleList.append((position, num))
                rainPositionStack.append(num)
        print("{},最后的tuple:{}".format(rainPositionStack, rainTupleList))
        allRain = 0
        for rainTuple in rainTupleList:
            leftHeight = rainTuple[0]
            rightHeight = rainTuple[1]
            minHeight = min(height[leftHeight], height[rightHeight])
            for i in range(leftHeight + 1, rightHeight):
                currentHeight = height[i]
                currentRain = minHeight - currentHeight
                allRain += currentRain
        return allRain


print(trap([0,1,0,2,1,0,1,3,0,1,2,1]))
