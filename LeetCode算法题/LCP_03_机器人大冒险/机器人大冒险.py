class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        u_num = 0
        r_num = 0
        fangxiang_set = []
        for position, zhiling in enumerate(command):
            if zhiling == "U":
                u_num += 1
            if zhiling == "R":
                r_num += 1
            if position != len(command) - 1:
                fangxiang_set.append((r_num, u_num))
        if not self.point_in_zoudao(x, y, u_num, r_num, fangxiang_set):
            return False
        else:
            for x_, y_ in obstacles:
                if x_ <= x and y_ <= y and self.point_in_zoudao(x_, y_, u_num, r_num, fangxiang_set):
                    return False
            return True

    def point_in_zoudao(self, x, y, u_num, r_num, fangxiang_set):
        if x == 0 and y == 0:
            return True
        if u_num == 0 and r_num == 0:
            if x != 0 or y != 0:
                return False
            else:
                return True
        elif u_num == 0:
            if y != 0:
                return False
            else:
                return True
        elif r_num == 0:
            if x != 0:
                return False
            else:
                return True

        bili_1 = x // r_num
        bili_2 = y // u_num
        min_bili = min(bili_1, bili_2)

        if x % r_num == 0 and y % u_num == 0 and x // r_num == y // u_num:
            return True
        x_yushu = x - min_bili * r_num
        y_yushu = y - min_bili * u_num
        if (x_yushu, y_yushu) in fangxiang_set:
            return True
        return False


solution = Solution()
print(solution.robot("URR", obstacles=[[2,2]], x=3,y=2))
