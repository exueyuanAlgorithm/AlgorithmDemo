class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=lambda key: len(key))
        result_list = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                words_1 = words[i]
                words_2 = words[j]
                if words_1 in words_2:
                    result_list.append(words_1)
                    break
        return result_list