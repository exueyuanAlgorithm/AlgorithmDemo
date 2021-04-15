class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        low_str = str(low)
        low_weishu = len(low_str)

        shouwei = int(low_str[0])
        weishu = low_weishu
        i = shouwei
        result_list = []
        while True:
            if i > 9 - weishu + 1:
                i = 1
                weishu += 1
                if weishu == 10:
                    break
                continue
            baocun_str = str(i)
            for wei in range(weishu-1):
                baocun_str += str(i+wei+1)
            baocun_int = int(baocun_str)
            if baocun_int > high:
                break
            if baocun_int >= low:
                result_list.append(baocun_int)
            i += 1
        return result_list


solution = Solution()
print(solution.sequentialDigits(58, 155))
