class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        num = 0
        qianzhui = ""
        yuansu = ""
        while True:
            for position, item in enumerate(strs):
                if num < len(item):
                    yuansu2 = item[num]
                    if position == 0:
                        yuansu = yuansu2
                    else:
                        if yuansu != yuansu2:
                            return qianzhui
                        elif position == len(strs) - 1:
                            qianzhui += yuansu
                            num += 1
                else:
                    return qianzhui

solution = Solution()
print(solution.longestCommonPrefix([]))