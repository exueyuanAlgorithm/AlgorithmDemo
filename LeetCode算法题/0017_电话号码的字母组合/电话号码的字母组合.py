class Solution(object):
    duiyingDict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        returnList = []
        for digit in digits:
            print(digit)
            if not returnList:
                for letter in Solution.duiyingDict[digit]:
                    returnList.append(letter)
            else:
                newList = []
                for letter in Solution.duiyingDict[digit]:
                    for alreadyHaveLetter in returnList:
                        newLetter = alreadyHaveLetter + letter
                        newList.append(newLetter)
                returnList.clear()
                returnList.extend(newList)

        return returnList

solution = Solution()
print(solution.letterCombinations("828"))