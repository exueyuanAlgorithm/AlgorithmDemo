class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        upCount = 0
        downCount = 0
        leftCount = 0
        rightCount = 0
        for move in moves:
            if move == "U":
                upCount += 1
            elif move == "D":
                downCount += 1
            elif move == "L":
                leftCount += 1
            elif move == "R":
                rightCount += 1
        if upCount == downCount and leftCount == rightCount:
            return True
        else:
            return False