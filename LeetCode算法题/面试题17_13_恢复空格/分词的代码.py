class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        wordNumDict = {}
        numArray = []
        for word in dictionary:
            numArray.append(len(word))
            wordNumArray = wordNumDict.get(len(word), [])
            wordNumArray.append(word)
            wordNumDict.setdefault(len(word), wordNumArray)
        numArray = sorted(list(set(numArray)), reverse=True)
        print(wordNumDict)
        print(numArray)
        i = 0
        forwordNotMatchList = []
        forwordMatchList = []
        while i < len(sentence):
            isBreak = False
            for letterNum in numArray:
                if i+letterNum <= len(sentence):
                    matchWord = sentence[i:i + letterNum]
                    if matchWord in wordNumDict[letterNum]:
                        print("匹配了:", matchWord)
                        forwordMatchList.append(matchWord)
                        i += len(matchWord)
                        isBreak = True
                        break
            else:
                forwordNotMatchList.append(sentence[i])
            if isBreak:
                continue
            i += 1
        # return notMathNum

        i = len(sentence)
        backWordNotMatchList = []
        backWordMatchList = []
        while i >= 1:
            isBreak = False
            for letterNum in numArray:
                if i - letterNum <= len(sentence):
                    matchWord = sentence[i-letterNum:i]
                    if matchWord in wordNumDict[letterNum]:
                        print("逆向匹配了:", matchWord)
                        backWordMatchList.append(matchWord)
                        i -= len(matchWord)
                        isBreak = True
                        break
            else:
                backWordNotMatchList.append(sentence[i-1])
            if isBreak:
                continue
            i -= 1
        print(len(forwordNotMatchList))
        print(len(backWordNotMatchList))
        print(forwordMatchList)
        print(list(reversed(backWordMatchList)))
        return min(len(forwordNotMatchList), len(backWordNotMatchList))


solution = Solution()
# dictionary = ["looked", "just", "like", "her", "brother"]
# sentence = "likejesslookedjustliketimherbrother"
dictionary = ["frrrbbrrbfrfqqbbbrb","qr","b","rf","qqbbbbfrqbrrqrffbrqqqbqqfqfrr","r","ffqq","bffbqfqqbrrrf","fq","qfr","fr","rqrrbfbfq","r","f","qbqbrbrbqfqbbbfbbbfbq","bqqbbbqrbbrf","f"]
sentence = "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"
solution.respace(dictionary, sentence)
