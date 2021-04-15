class Solution(object):
    def get_quan_num(self, pos, num):
        if num % 2 == 0:
            if pos < num // 2:
                max_pos = pos
            else:
                max_pos = num - pos - 1
        else:
            if pos <= num // 2:
                max_pos = pos
            else:
                max_pos = num - pos - 1
        return max_pos

    def orchestraLayout(self, num, xPos, yPos):
        """
        :type num: int
        :type xPos: int
        :type yPos: int
        :rtype: int
        """
        # 计算每一圈顶点位置的序号
        # 已知xPos， yPos，求所处的圈圈
        quan_num = min(self.get_quan_num(xPos, num), self.get_quan_num(yPos, num))
        quan_left_top_position = 4 * (quan_num * num - quan_num * quan_num)

        left_top = quan_num
        right_bottom = quan_num + (num - 1 - 2 * quan_num)
        zengjia_num = num - 1 - 2 * quan_num
        add_num = 0
        if xPos == left_top and left_top <= yPos <= right_bottom:
            add_num += yPos - left_top
        elif yPos == right_bottom and left_top < xPos <= right_bottom:
            add_num += zengjia_num + xPos - left_top
        elif xPos == right_bottom and left_top <= yPos < right_bottom:
            add_num += 2 * zengjia_num + right_bottom - yPos
        elif yPos == left_top and left_top < xPos < right_bottom:
            add_num += 3 * zengjia_num + right_bottom - xPos

        return (quan_left_top_position + add_num) % 9 + 1


solution = Solution()
print(solution.orchestraLayout(4, 1, 2))
