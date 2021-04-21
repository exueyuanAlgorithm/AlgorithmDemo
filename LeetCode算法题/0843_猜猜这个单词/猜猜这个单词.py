import random
from collections import Counter


class Master(object):
    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        # print(word, self.secret)
        num = 0
        for item1, item2 in zip(word, self.secret):
            if item1 == item2:
                num += 1
        return num


class Solution(object):
    def __init__(self):
        self.guess_num = 0

    def get_match_num(self, word1, word2):
        """
        :type word: str
        :rtype int
        """
        num = 0
        for item1, item2 in zip(word1, word2):
            if item1 == item2:
                num += 1
        return num

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        counter_list = [{} for _ in range(6)]
        for word in wordlist:
            for position, item in enumerate(word):
                counter_list[position][item] = counter_list[position].get(item, 0) + 1
        max_word = None
        max_score = -1000
        for word in wordlist:
            score = 0
            for position, item in enumerate(word):
                score += counter_list[position].get(item, 0)
                if score > max_score:
                    max_word = word
                    max_score = score
        match_num = master.guess(max_word)
        self.guess_num += 1
        if match_num == 6:
            return True
        word_length = len(wordlist)
        for i in range(word_length - 1, -1, -1):
            word2 = wordlist[i]
            if self.get_match_num(max_word, word2) != match_num:
                wordlist.pop(i)
        self.findSecretWord(wordlist, master)


def create_word():
    return ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd',
         'c', 'b', 'a'], 6))


def create_word_list():
    wordlist = [create_word() for _ in range(100)]
    num = random.randint(0, 99)
    secret = wordlist[num]
    return wordlist, secret


for i in range(1000):
    solution = Solution()
    wordlist, secret = create_word_list()
    master = Master(secret)
    solution.findSecretWord(wordlist, master)
    print(solution.guess_num)
