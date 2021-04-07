class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        position = 0
        while True:
            if position < len(s):
                item = s[position]
            else:
                return num
            if position + 1 < len(s):
                next_item = s[position + 1]
            else:
                next_item = None
            if position + 2 < len(s):
                next_next_item = s[position + 2]
            else:
                next_next_item = None
            if position + 3 < len(s):
                next_next_next_item = s[position + 3]
            else:
                next_next_next_item = None
            if item == "M":
                if next_item == "M" and next_next_item == "M":
                    num += 3000
                    position += 3
                elif next_item == "M":
                    num += 2000
                    position += 2
                else:
                    num += 1000
                    position += 1
            elif item == "C":
                if next_item == "D":
                    num += 400
                    position += 2
                elif next_item == "M":
                    num += 900
                    position += 2
                elif next_item == "C" and next_next_item == "C":
                    num += 300
                    position += 3
                elif next_item == "C":
                    num += 200
                    position += 2
                else:
                    num += 100
                    position += 1
            elif item == "D":
                if next_item == "C" and next_item == next_next_item == next_next_next_item:
                    num += 800
                    position += 4
                elif next_item == "C" and next_item == next_next_item:
                    num += 700
                    position += 3
                elif next_item == "C":
                    num += 600
                    position += 2
                else:
                    num += 500
                    position += 1
            elif item == "X":
                if next_item == "L":
                    num += 40
                    position += 2
                elif next_item == "C":
                    num += 90
                    position += 2
                elif next_item == "X" and next_next_item == "X":
                    num += 30
                    position += 3
                elif next_item == "X":
                    num += 20
                    position += 2
                else:
                    num += 10
                    position += 1
            elif item == "L":
                if next_item == "X" and next_item == next_next_item == next_next_next_item:
                    num += 80
                    position += 4
                elif next_item == "X" and next_item == next_next_item:
                    num += 70
                    position += 3
                elif next_item == "X":
                    num += 60
                    position += 2
                else:
                    num += 50
                    position += 1
            elif item == "I":
                if next_item == "V":
                    num += 4
                    position += 2
                elif next_item == "X":
                    num += 9
                    position += 2
                elif next_item == "I" and next_next_item == "I":
                    num += 3
                    position += 3
                elif next_item == "I":
                    num += 2
                    position += 2
                else:
                    num += 1
                    position += 1
            elif item == "V":
                if next_item == "I" and next_item == next_next_item == next_next_next_item:
                    num += 8
                    position += 4
                elif next_item == "I" and next_item == next_next_item:
                    num += 7
                    position += 3
                elif next_item == "I":
                    num += 6
                    position += 2
                else:
                    num += 5
                    position += 1


