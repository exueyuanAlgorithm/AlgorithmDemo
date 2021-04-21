class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num_str = "1"
        for _ in range(n - 1):
            count = 0
            num_item = ""
            result_str = ""
            for position, item in enumerate(num_str):
                if position == 0:
                    count = 1
                    num_item = item
                    continue
                if num_str[position - 1] == item:
                    count += 1
                else:
                    result_str += str(count) + num_item
                    count = 1
                    num_item = item
            result_str += str(count) + num_item
            num_str = result_str
        return num_str
solution = Solution()
print(solution.countAndSay(5))
