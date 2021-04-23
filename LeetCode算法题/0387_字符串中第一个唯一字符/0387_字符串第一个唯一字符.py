class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_set = set()
        for i in range(len(s)):
            item1 = s[i]
            if item1 in str_set:
                continue
            is_find = True
            for j in range(i + 1, len(s)):
                item2 = s[j]
                if item1 == item2:
                    is_find = False
                    str_set.add(item1)
                    break
            if is_find:
                return i
        return -1
