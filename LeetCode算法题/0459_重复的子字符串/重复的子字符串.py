class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sLen = len(s)
        middleNum = sLen // 2

        if sLen <= 1:
            return False

        for i in range(1, middleNum + 1):
            word = s[:i]
            wordCount = 0
            while wordCount < sLen:
                rightLine = min(sLen, wordCount + len(word))
                newWord = s[wordCount:rightLine]
                wordCount = rightLine
                print(word, newWord, rightLine)
                if word != newWord:
                    break
                if wordCount == sLen:
                    return True
        return False



        # if sLen % 2 == 1:
        #     word = s[0]
        #     for item in s:
        #         if item != word:
        #             return False
        #     return True
        # if sLen % 2 == 0:
        #     left = s[:middleNum]
        #     right = s[middleNum:]
        #     if left == right:
        #         return True
        #     else:
        #         return False

solution = Solution()
print(solution.repeatedSubstringPattern("ababab"))