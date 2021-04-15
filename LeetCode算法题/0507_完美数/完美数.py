import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        sum_ = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(i)
                if i == num // i:
                    sum_ += i
                else:
                    sum_ += i
                    if num // i != num:
                        print(num // i)
                        sum_ += num // i
        if sum_ == num:
            return True
        else:
            return False
solution = Solution()
print(solution.checkPerfectNumber(1))