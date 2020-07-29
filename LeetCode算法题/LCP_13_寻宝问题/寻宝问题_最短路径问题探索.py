import copy


class Solution:
    # 上，右，下，左
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def checkIsValidStep(self, maze, x, y, dp_already = None):
        """
        验证 x，y点在maze上是不是有效的
        :param dp_already:
        :param maze: 地图
        :param x:
        :param y:
        :return: 是否有效，人是否可以站在这里
        """
        if x < 0 or x >= len(maze):
            return False
        if y < 0 or y >= len(maze[0]):
            return False
        if maze[x][y] == "#":
            return False
        if dp_already and dp_already[x][y] == 1:
            return False
        return True

    def minStepFromStartToTarget(self, maze, startTuple, targetTuple):
        """
        检测从start 到 target的最短路径步数
        :param maze 地图 ["S#O", "M..", "M.T"]
        :param startTuple: X的起始点坐标 (0, 1)
        :param targetTuple: Y的目标点坐标 (3, 4)
        :return:
        """
        m = len(maze)
        n = len(maze[0])
        dp = [[-1] * n for _ in range(m)]
        dp_already = [[0] * n for _ in range(m)]
        currentDistance = 0
        dp[startTuple[0]][startTuple[1]] = 0
        dp_already[startTuple[0]][startTuple[1]] = 1
        alreadyHaveDistancePositionList = [startTuple]

        while alreadyHaveDistancePositionList:
            alreadyHaveDistancePositionListCopy = []
            alreadyHaveDistancePositionListCopy.extend(alreadyHaveDistancePositionList)
            alreadyHaveDistancePositionList.clear()
            currentDistance += 1
            for position in alreadyHaveDistancePositionListCopy:
                for dir in Solution.dirs:
                    new_position = position[0] + dir[0], position[1] + dir[1]
                    if self.checkIsValidStep(maze, new_position[0], new_position[1], dp_already):
                        dp[new_position[0]][new_position[1]] = currentDistance
                        dp_already[new_position[0]][new_position[1]] = 1
                        if new_position == targetTuple:
                            return currentDistance
                        alreadyHaveDistancePositionList.append(new_position)
        return -1

    def getSimplifyDistanceDict(self, distanceDict, start_position, target_position, stone_position_list, gear_position_list):
        simplifyDistanceDict = {}
        # 先算起始点到所有机关点的距离
        for stone_position in stone_position_list:
            for gear_position in gear_position_list:
                distance1 = distanceDict[(start_position, stone_position)]
                distance2 = distanceDict[(gear_position, stone_position)]
                if distance1 >= 0 and distance2 >= 0:
                    distance = simplifyDistanceDict.get((start_position, gear_position), -1)
                    sumDistance = distance1 + distance2
                    if sumDistance <= distance or distance == -1:
                        simplifyDistanceDict[(start_position, gear_position)] = sumDistance
                else:
                    simplifyDistanceDict[(start_position, gear_position)] = -1
        # 计算所有机关点到机关点的距离
        for gear_position_1 in gear_position_list:
            for gear_position_2 in gear_position_list:
                for stone_position in stone_position_list:
                    if gear_position_1 == gear_position_2:
                        break
                    distance1 = distanceDict[(gear_position_1, stone_position)]
                    distance2 = distanceDict[(gear_position_2, stone_position)]
                    if distance1 >= 0 and distance2 >= 0:
                        distance = simplifyDistanceDict.get((gear_position_1, gear_position_2), -1)
                        sumDistance = distance1 + distance2
                        if sumDistance <= distance or distance == -1:
                            simplifyDistanceDict[(gear_position_1, gear_position_2)] = sumDistance
                    else:
                        simplifyDistanceDict[(gear_position_1, gear_position_2)] = -1
        # 计算所有机关点到终点的距离
        for gear_position in gear_position_list:
            simplifyDistanceDict[(gear_position, target_position)] = distanceDict[(gear_position, target_position)]
        return simplifyDistanceDict

    def getDistanceDict(self, maze, start_position, target_position, stone_position_list, gear_position_list):
        distanceDict = {}
        # 首先起始点到终点的距离
        distanceDict[(start_position, target_position)] = self.minStepFromStartToTarget(maze, start_position, target_position)
        # 计算起始点到每个石堆的距离
        for stone_position in stone_position_list:
            distanceDict[(start_position, stone_position)] = self.minStepFromStartToTarget(maze, start_position, stone_position)
        # 计算所有石堆到M的距离
        for stone_position in stone_position_list:
            for gear_position in gear_position_list:
                distance = self.minStepFromStartToTarget(maze, stone_position, gear_position)
                distanceDict[(gear_position, stone_position)] = distance
        # 计算所有M到target的距离
        for gear_position in gear_position_list:
            distanceDict[(gear_position, target_position)] = self.minStepFromStartToTarget(maze, gear_position, target_position)
        return distanceDict

    def getMinimalStepsFromAToBRoutC(self, startPosition, targetPosition, routPositionList:list, simplifyDistanceDict):
        print(routPositionList)
        if not routPositionList:
            return simplifyDistanceDict[startPosition, targetPosition]

        miniDistance = -1
        for routPosition in routPositionList:
            newRoutPositionList = copy.deepcopy(routPositionList)
            newRoutPositionList.remove(routPosition)
            distance1 = simplifyDistanceDict[(startPosition, routPosition)]
            if distance1 >= 0:
                distance2 = self.getMinimalStepsFromAToBRoutC(routPosition, targetPosition, newRoutPositionList, simplifyDistanceDict)
                if distance2 >= 0:
                    all_distance = distance1 + distance2
                    if all_distance < miniDistance or miniDistance == -1:
                        miniDistance = all_distance
        return miniDistance


    def minimalSteps(self, maze: list) -> int:
        """
        :param maze: ["S#O", "M..", "M.T"]
        :return:
        """
        start_position = None
        target_position = None
        stone_position_list = []
        gear_position_list = []
        for i, line in enumerate(maze):
            for j, item_str in enumerate(line):
                if item_str == "S":
                    start_position = (i, j)
                elif item_str == "T":
                    target_position = (i, j)
                elif item_str == "O":
                    stone_position_list.append((i, j))
                elif item_str == "M":
                    gear_position_list.append((i, j))
        distanceDict = self.getDistanceDict(maze, start_position, target_position, stone_position_list, gear_position_list)

        # print(distanceDict)

        if not gear_position_list:
            return distanceDict[(start_position, target_position)]

        simplifyDistanceDict = self.getSimplifyDistanceDict(distanceDict, start_position, target_position, stone_position_list, gear_position_list)
        print(simplifyDistanceDict)
        return self.getMinimalStepsFromAToBRoutC(start_position, target_position, gear_position_list, simplifyDistanceDict)





solution = Solution()
# print(solution.minimalSteps(
#     ["......",
#      "M....M",
#      ".M#...",
#      "....M.",
#      "##.TM.",
#      "...O..",
#      ".S##O.",
#      "M#..M.",
#      "#....."]))
print(solution.minimalSteps(["M...M","MS#MM","MM#TO"]))
# print(solution.minimalSteps(
#     ["S#O", "M..", "M.T"]
# ))

# a = tuple({(3, 2), (5, 7)})
# print(a)
# b = tuple({(5, 7), (3, 2)})
# print(a == b)
#
# c = {a:"8"}



