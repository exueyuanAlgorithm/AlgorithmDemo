class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        # dict = {
        #     "a": {"c": {},
        #           "d": {}},
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
                    lastDict.setdefault("end", True)
                lastDict = newDict
        print(letterDict)

        dp = [0]*(len(sentence)+1)
        for i in range(1, len(sentence)+1):
            dp[i] = dp[i-1] + 1
            for idx in range(0, i):
                if sentence[idx:i] in dictionary:
                    dp[i] = min(dp[i], dp[idx])
        return dp[len(sentence)]


solution = Solution()
dictionary = ["looked", "just", "like", "her", "brother"]
sentence = "likejesslookedjustliketimherbrother"
# dictionary = ["frrrbbrrbfrfqqbbbrb","qr","b","rf","qqbbbbfrqbrrqrffbrqqqbqqfqfrr","r","ffqq","bffbqfqqbrrrf","fq","qfr","fr","rqrrbfbfq","r","f","qbqbrbrbqfqbbbfbbbfbq","bqqbbbqrbbrf","f"]
# sentence = "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"
solute = solution.respace(dictionary, sentence)
print(solute)