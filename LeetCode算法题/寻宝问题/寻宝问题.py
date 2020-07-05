

class Solution:
    # 上，右，下，左
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def checkIsValidStep(self, maze, x, y):
        """
        验证 x，y点在maze上是不是有效的
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
        if maze[x][y] == "2":
            return False
        return True

    def checkIsValidStepAndStack(self, maze_array, nextp):
        x = nextp[0]
        y = nextp[1]
        return self.checkIsValidStep(maze_array, x, y)

    def mark(self, maze_array, pos):  # 给迷宫maze的位置pos标"2"表示“倒过了”
        maze_array[pos[0]][pos[1]] = "2"

    def unmark(self, maze_array, pos):
        maze_array[pos[0]][pos[1]] = "."

    def minStepFromStartToTarget(self, maze, startTuple, targetTuple):
        """
        :param maze 地图 ["S#O", "M..", "M.T"]
        :param startTuple: X的起始点坐标 (0, 1)
        :param targetTuple: Y的目标点坐标 (3, 4)
        :return:
        """
        if startTuple == targetTuple:
            print(startTuple)
        new_maze = []
        for direct_str in maze:
            maze_hang = []
            for str_item in direct_str:
                maze_hang.append(str_item)
            new_maze.append(maze_hang)
        positionDirectionStack = [(startTuple, 0)]
        self.mark(new_maze, startTuple)
        minStep = None
        while positionDirectionStack:
            pos, nxt = positionDirectionStack.pop()
            for i in range(nxt, 4):
                nextp = pos[0] + Solution.dirs[i][0], pos[1] + Solution.dirs[i][1]
                if nextp == targetTuple:
                    positionDirectionStack.append((pos, i + 1))
                    positionDirectionStack.append((nextp, 0))
                    # print(positionDirectionStack)
                    stepNum = len(positionDirectionStack) - 1
                    if minStep is None:
                        minStep = stepNum
                    else:
                        if stepNum < minStep:
                            minStep = stepNum
                    positionDirectionStack.pop()
                    break
                if self.checkIsValidStepAndStack(new_maze, nextp):
                    positionDirectionStack.append((pos, i + 1))
                    self.mark(new_maze, nextp)
                    positionDirectionStack.append((nextp, 0))
                    break
            else:
                self.unmark(new_maze, pos)
        return minStep

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
                distanceDict[(stone_position, gear_position)] = distance
                distanceDict[(gear_position, stone_position)] = distance
        # 计算所有M到target的距离
        for gear_position in gear_position_list:
            distanceDict[(gear_position, target_position)] = self.minStepFromStartToTarget(maze, gear_position, target_position)
        return distanceDict

    def calculateDistance(self, distanceStack, distanceDict):
        """
        计算距离
        :param distanceStack:
        :param distanceDict:
        :return:
        """
        allStep = 0
        for i, position in enumerate(distanceStack):
            if i+1 < len(distanceStack):
                nextPosition = distanceStack[i+1]
                allStep += distanceDict[(position[0], nextPosition[0])]
        return allStep


    def minimalSteps(self, maze: list) -> int:
        """
        :param maze: ["S#O", "M..", "M.T"]
        :return:
        """
        start_position = None
        target_position = None
        stone_position_list = []
        gear_position_list = []
        already_gear_position_list_flag = []
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
                    already_gear_position_list_flag.append([(i, j), False])
        distanceDict = self.getDistanceDict(maze, start_position, target_position, stone_position_list, gear_position_list)

        print(distanceDict)

        if not gear_position_list:
            distance = distanceDict[(start_position, target_position)]
            if distance is None:
                return -1
            return distance

        minStep = None
        # 栈里存放的是当前位置，下一个位置的探索点
        distanceStack = [(start_position, 0)]
        while distanceStack:
            currentPosition, nextXulie = distanceStack.pop()
            if currentPosition == start_position:
                for i in range(nextXulie, len(stone_position_list)):
                    distance = distanceDict[(currentPosition, stone_position_list[i])]
                    if distance is not None:
                        distanceStack.append((currentPosition, i + 1))
                        distanceStack.append((stone_position_list[i], 0))
                        break
            elif currentPosition in stone_position_list:
                for i in range(nextXulie, len(gear_position_list)):
                    if not already_gear_position_list_flag[i][1]:
                        distance = distanceDict[(currentPosition, gear_position_list[i])]
                        if distance is not None:
                            distanceStack.append((currentPosition, i + 1))
                            distanceStack.append((gear_position_list[i], 0))
                            already_gear_position_list_flag[i][1] = True
                            break
            elif currentPosition in gear_position_list:
                all_already_gear_flag = True
                for already_gear_position_flag in already_gear_position_list_flag:
                    if not already_gear_position_flag[1]:
                        all_already_gear_flag = False
                        break
                isAttend = False
                if all_already_gear_flag:
                    distance = distanceDict[(currentPosition, target_position)]
                    if distance is not None and nextXulie == 0:
                        isAttend = True
                        # 找终点
                        distanceStack.append((currentPosition, nextXulie+1))
                        distanceStack.append((target_position, 0))
                        print(distanceStack)
                        allDistance = self.calculateDistance(distanceStack, distanceDict)
                        print("距离为:{}".format(allDistance))
                        if minStep is None:
                            minStep = allDistance
                        else:
                            if allDistance < minStep:
                                minStep = allDistance
                        distanceStack.pop()
                else:
                    # 找石堆
                    for i in range(nextXulie, len(stone_position_list)):
                        distance = distanceDict[(currentPosition, stone_position_list[i])]
                        if distance is not None:
                            isAttend = True
                            distanceStack.append((currentPosition, i + 1))
                            distanceStack.append((stone_position_list[i], 0))
                            break
                if not isAttend:
                    for already_gear in already_gear_position_list_flag:
                        if currentPosition == already_gear[0]:
                            already_gear[1] = False

        if minStep is None:
            return -1
        else:
            return minStep


solution = Solution()
print(solution.minimalSteps(["......", "M....M", ".M#...", "....M.", "##.TM.", "...O..", ".S##O.", "M#..M.", "#....."]))
# print(solution.checkIsValidStep(["S#O", "M..", "M.T"], 1, 0))
# print(solution.minStepFromStartToTarget(["S#O", "...", "M.T"], (0,0),(2,2)))
