class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        # dict = {
        #     "a": {"c": {},
        #           "d": {},
        #           "end"},
        #     "b": {},
        #     "c": {},
        # }
        letterDict = {}
        for word in dictionary:
            lastDict = letterDict
            for i, letter in enumerate(reversed(word)):
                newDict = lastDict.get(letter, {})
                if letter not in lastDict:
                    lastDict.setdefault(letter, newDict)
                if i == len(word)-1:
                    newDict.setdefault("end", True)
                lastDict = newDict
        print(letterDict)

        dp = [0]*(len(sentence)+1)
        for i in range(1, len(sentence)+1):
            dp[i] = dp[i-1] + 1
            # lastDict = letterDict
            # 遍历 (i-1) - 0
            #
            # a = sententce[idx]
            # 判断 a 是否在lastDict中，不在的话，直接结束判断
            # 在的话，判断是否是end
            #   是end的话，那么 进行判断
            #   dp[i] = min(dp[i], dp[idx])
            # 那么 lastDict = lastDict[a]
            #
            lastDict = letterDict
            for idx in range(i-1, -1, -1):
                letter = sentence[idx]
                if letter in lastDict:
                    lastDict = lastDict[letter]
                    if lastDict.get("end", False):
                        dp[i] = min(dp[i], dp[idx])
                else:
                    break
        print(dp)
        return dp[len(sentence)]


solution = Solution()
# dictionary = ["looked", "just", "like", "her", "brother"]
# sentence = "likejesslookedjustliketimherbrother"
# dictionary = ["frrrbbrrbfrfqqbbbrb","qr","b","rf","qqbbbbfrqbrrqrffbrqqqbqqfqfrr","r","ffqq","bffbqfqqbrrrf","fq","qfr","fr","rqrrbfbfq","r","f","qbqbrbrbqfqbbbfbbbfbq","bqqbbbqrbbrf","f"]
# sentence = "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"
dictionary = ["wccm","wiw","uwwiwcmiiiwmmwicuwu","mw"]
sentence = "iwiwwwmuiccwwwwwmumwwwmcciwwuiwcicwwuwicuiwciwmiwicwuwwmuimccwucuuim"
solute = solution.respace(dictionary, sentence)
print(solute)