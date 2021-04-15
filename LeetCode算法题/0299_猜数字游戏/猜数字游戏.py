class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        gongniu = 0
        i = 0
        while True:
            if i >= len(secret):
                break
            item1 = secret[i]
            item2 = guess[i]
            if item1 == item2:
                gongniu += 1
                secret = secret[:i] + secret[i+1:]
                guess = guess[:i] + guess[i+1:]
            else:
                i += 1
        nainiu = 0
        i = 0
        while True:
            if i >= len(secret):
                break
            item1 = secret[i]
            j = guess.find(item1)
            if j >= 0:
                nainiu += 1
                secret = secret[:i] + secret[i + 1:]
                guess = guess[:j] + guess[j + 1:]
            else:
                i += 1
        return str(gongniu) + "A" + str(nainiu) + "B"
solution = Solution()
solution.getHint("1807", "7817")

