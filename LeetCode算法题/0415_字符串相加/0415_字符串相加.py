class Solution(object):
    tryAddList = [("0", "0", "0", False),
                  ("0", "1", "1", False),
                  ("0", "2", "2", False),
                  ("0", "3", "3", False),
                  ("0", "4", "4", False),
                  ("0", "5", "5", False),
                  ("0", "6", "6", False),
                  ("0", "7", "7", False),
                  ("0", "8", "8", False),
                  ("0", "9", "9", False),
                  ("1", "1", "2", False),
                  ("1", "2", "3", False),
                  ("1", "3", "4", False),
                  ("1", "4", "5", False),
                  ("1", "5", "6", False),
                  ("1", "6", "7", False),
                  ("1", "7", "8", False),
                  ("1", "8", "9", False),
                  ("1", "9", "0", True),
                  ("2", "2", "4", False),
                  ("2", "3", "5", False),
                  ("2", "4", "6", False),
                  ("2", "5", "7", False),
                  ("2", "6", "8", False),
                  ("2", "7", "9", False),
                  ("2", "8", "0", True),
                  ("2", "9", "1", True),
                  ("3", "3", "6", False),
                  ("3", "4", "7", False),
                  ("3", "5", "8", False),
                  ("3", "6", "9", False),
                  ("3", "7", "0", True),
                  ("3", "8", "1", True),
                  ("3", "9", "2", True),
                  ("4", "4", "8", False),
                  ("4", "5", "9", False),
                  ("4", "6", "0", True),
                  ("4", "7", "1", True),
                  ("4", "8", "2", True),
                  ("4", "9", "3", True),
                  ("5", "5", "0", True),
                  ("5", "6", "1", True),
                  ("5", "7", "2", True),
                  ("5", "8", "3", True),
                  ("5", "9", "4", True),
                  ("6", "6", "2", True),
                  ("6", "7", "3", True),
                  ("6", "8", "4", True),
                  ("6", "9", "5", True),
                  ("7", "7", "4", True),
                  ("7", "8", "5", True),
                  ("7", "9", "6", True),
                  ("8", "8", "6", True),
                  ("8", "9", "7", True),
                  ("9", "9", "8", True)]

    def tryAdd(self, num1, num2):
        for tryAddTuple in Solution.tryAddList:
            if (num1 == tryAddTuple[0] and num2 == tryAddTuple[1]) or (num1 == tryAddTuple[1] and num2 == tryAddTuple[0]):
                return tryAddTuple[2], tryAddTuple[3]

    def getNumStr(self, num1, position):
        num1_result = num1[::-1]
        if position < len(num1):
            return num1_result[position]
        else:
            return "0"

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lenNum1 = len(num1)
        lenNum2 = len(num2)
        needAndOne = False
        resultNum = ""
        for i in range(max(lenNum1, lenNum2)):
            addNum1 = self.getNumStr(num1, i)
            addNum2 = self.getNumStr(num2, i)
            result, needAddOne_1 = self.tryAdd(addNum1, addNum2)
            needAndOne_2 = False
            if needAndOne:
                result, needAndOne_2 = self.tryAdd(result, "1")
            needAndOne = needAddOne_1 or needAndOne_2
            resultNum += result
        if needAndOne:
            resultNum += "1"
        return resultNum[::-1]


solution = Solution()
print(solution.addStrings("6", "501"))
