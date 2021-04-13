class Solution(object):
    num_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    def add(self, num1, num2):
        m_sum = ""
        jinyi = 0
        for i in range(0, max(len(num1), len(num2))):
            wei1_position = len(num1) - 1 - i
            if wei1_position >= 0:
                wei1_str = num1[wei1_position]
                wei1 = Solution.num_dict[wei1_str]
            else:
                wei1 = 0
            wei2_position = len(num2) - 1 - i
            if wei2_position >= 0:
                wei2_str = num2[wei2_position]
                wei2 = Solution.num_dict[wei2_str]
            else:
                wei2 = 0

            he = wei1 + wei2 + jinyi
            if he >= 10:
                jinyi = 1
            else:
                jinyi = 0
            m_sum = str(he % 10) + m_sum
        if jinyi == 1:
            m_sum = "1" + m_sum
        return m_sum

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        sum_ = ""
        for i in range(len(num1)):
            num_str_1 = num1[len(num1)-i-1]
            num_1 = Solution.num_dict[num_str_1]
            for j in range(len(num2)):
                num_str_2 = num2[len(num2)-j-1]
                num_2 = Solution.num_dict[num_str_2]
                sum_ = self.add(sum_, str(num_1 * num_2) + "0"*(i+j))
        return sum_


solution = Solution()
print(solution.multiply("283", "984"))
