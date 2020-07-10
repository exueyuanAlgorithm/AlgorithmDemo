class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanStr = ""
        qian = num // 1000
        if qian > 0:
            for i in range(qian):
                romanStr += "M"
        bai = (num // 100) % 10
        if bai > 0:
            if bai <= 3:
                for i in range(bai):
                    romanStr += "C"
            elif bai == 4:
                romanStr += "CD"
            elif bai == 9:
                romanStr += "CM"
            else:
                romanStr += "D"
                for i in range(bai - 5):
                    romanStr += "C"

        ten = (num // 10) % 10
        if ten > 0:
            if ten <= 3:
                for i in range(ten):
                    romanStr += "X"
            elif ten == 4:
                romanStr += "XL"
            elif ten == 9:
                romanStr += "XC"
            else:
                romanStr += "L"
                for i in range(ten - 5):
                    romanStr += "X"

        ge = num % 10
        if ge > 0:
            if ge <= 3:
                for i in range(ge):
                    romanStr += "I"
            elif ge == 4:
                romanStr += "IV"
            elif ge == 9:
                romanStr += "IX"
            else:
                romanStr += "V"
                for i in range(ge - 5):
                    romanStr += "I"
        return romanStr


solution = Solution()
print(solution.intToRoman(9))