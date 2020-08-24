class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        dui = 0
        for i,b in enumerate(guess):
            a = answer[i]
            if a == b:
                dui += 1
        return dui