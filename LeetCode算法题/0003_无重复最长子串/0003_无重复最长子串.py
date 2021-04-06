
def func(s):
    zichuan = ""
    max_length = 0
    for position, item in enumerate(s):
        weizhi = zichuan.find(item)
        if weizhi == -1:
            zichuan += item
        else:
            if len(zichuan) > max_length:
                max_length = len(zichuan)
            zichuan = zichuan[weizhi+1:] + item
    if len(zichuan) > max_length:
        max_length = len(zichuan)
    return max_length

print(func("a"))


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        zichuan = ""
        max_length = 0
        for position, item in enumerate(s):
            weizhi = zichuan.find(item)
            if weizhi == -1:
                zichuan += item
            else:
                if len(zichuan) > max_length:
                    max_length = len(zichuan)
                zichuan = zichuan[weizhi + 1:] + item
        if len(zichuan) > max_length:
            max_length = len(zichuan)
        return max_length

