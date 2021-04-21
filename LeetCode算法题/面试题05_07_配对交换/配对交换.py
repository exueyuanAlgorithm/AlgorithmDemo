class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        weishu = 0
        while True:
            if num < pow(2, weishu):
                break
            weishu += 1

        new_num = 0
        i = 0
        while True:
            if i >= weishu:
                break
            mowei_1 = 1 if num % 2 == 1 else 0
            num = num >> 1
            mowei_2 = 1 if num % 2 == 1 else 0
            num = num >> 1
            zuoyi_test = mowei_1 << 1
            add_num = zuoyi_test + mowei_2
            zuoyi_2_test = add_num << i
            new_num = zuoyi_2_test + new_num
            i += 2
        return new_num

solution = Solution()
solution.exchangeBits(0b00)