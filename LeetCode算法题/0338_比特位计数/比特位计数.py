class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits_num_list = []
        for i in range(num+1):
            if i == 0:
                bits_num_list.append(i)
            else:
                last_num = i-1
                delete_num = 0
                while last_num & 1 == 1:
                    delete_num += 1
                    last_num >>= 1
                delete_num -= 1
                bits_num_list.append(bits_num_list[i-1] - delete_num)
        return bits_num_list

solution = Solution()
print(solution.countBits(8))