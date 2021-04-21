class Solution(object):
    def numDecodings_dict(self, s, huancun_dict):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith("0"):
            return 0
        if not s:
            return 1
        if s in huancun_dict:
            return huancun_dict[s]
        # 分为两种情况，前一位，或者前两位
        qingkuang1 = self.numDecodings_dict(s[1:], huancun_dict)
        # 前两位的情况：
        qingkuang2 = 0
        if len(s) >= 2:
            num2 = int(s[:2])
            if 1 <= num2 <= 26:
                qingkuang2 = self.numDecodings_dict(s[2:], huancun_dict)
        huancun_dict[s] = qingkuang1 + qingkuang2
        return qingkuang1 + qingkuang2

    def numDecodings(self, s):
        return self.numDecodings_dict(s, {})

