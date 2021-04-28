class Solution(object):
    def check_word1_word2(self, word1, word2):
        lenth1 = len(word1)
        lenth2 = len(word2)
        if lenth2 - lenth1 != 1:
            return False
        i = 0
        j = 0
        is_different = False
        while True:
            if i >= len(word1):
                return True
            item1 = word1[i]
            item2 = word2[j]
            if item1 != item2:
                if is_different:
                    return False
                else:
                    is_different = True
                    j += 1
            else:
                i += 1
                j += 1

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda item: len(item))
        length_start_dict = {}
        for position, word in enumerate(words):
            length = len(word)
            if length not in length_start_dict:
                length_start_dict[length] = position
        words_length = len(words)
        dp = [1] * words_length
        for position, word in enumerate(words):
            word_len = len(word)
            if word_len == 1:
                dp[position] = 1
                continue
            dp[position] = 1
            if word_len - 1 in length_start_dict:
                for j in range(length_start_dict[word_len - 1], position):
                    word1 = words[j]
                    if len(word1) != word_len - 1:
                        break
                    if self.check_word1_word2(word1, word):
                        dp[position] = max(dp[position], dp[j] + 1)
        return max(dp)
