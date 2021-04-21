class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        time_list = []
        for item in time:
            time_list.append(item % 60)
        time_list.sort()
        i = 0
        j = len(time_list) - 1
        zero_num = 0
        thirty_num = 0
        all_num = 0
        while i < j:
            if time_list[i] == 0:
                zero_num += 1
                i += 1
                while i < len(time_list) and time_list[i] == 0:
                    zero_num += 1
                    i += 1
            if i >= j:
                break
            num1 = time_list[i]
            num2 = time_list[j]
            if num1 == 30:
                thirty_num += 1
                i += 1
                while i < len(time_list) and time_list[i] == 30:
                    thirty_num += 1
                    i += 1
                break
            elif num1 + num2 == 60:
                num1_num = 1
                i += 1
                while i < j and time_list[i] == num1:
                    num1_num += 1
                    i += 1
                num2_num = 1
                j -= 1
                while i < j and time_list[j] == num2:
                    num2_num += 1
                    j -= 1
                all_num += num1_num * num2_num
            elif num1 + num2 < 60:
                i += 1
            elif num1 + num2 > 60:
                j -= 1

        all_num += zero_num * (zero_num - 1) // 2
        all_num += thirty_num * (thirty_num - 1) // 2
        return all_num


solution = Solution()
print(solution.numPairsDivisibleBy60([60, 60, 60]))
