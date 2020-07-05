class Solution:
    def longestValidParentheses(self, s: str) -> int:
        kuohaoStack = []
        kuohaoMatch = []
        positionBiaoJi = [0] * len(s)
        for s_i, ss in enumerate(s):
            if ss == "(":
                kuohaoStack.append(s_i)
            else:
                if kuohaoStack:
                    leftPosition = kuohaoStack.pop()
                    positionBiaoJi[leftPosition] = 1
                    positionBiaoJi[s_i] = 1
                    kuohaoMatch.append((leftPosition, s_i))
        print(kuohaoMatch)
        print(positionBiaoJi)

        maxMatchLength = 0
        currentMatchLength = 0
        for i in positionBiaoJi:
            if i == 1:
                currentMatchLength += 1
            else:
                if currentMatchLength > maxMatchLength:
                    maxMatchLength = currentMatchLength
                currentMatchLength = 0
        else:
            if currentMatchLength > maxMatchLength:
                maxMatchLength = currentMatchLength
        return maxMatchLength


solution = Solution()
print(solution.longestValidParentheses("(()"))