class Solution(object):
    def get_sum_geti(self, n):
        i = 1
        sum_geti = 0
        while True:
            yushu = n % pow(10, i)
            shang = yushu // pow(10, i - 1)
            geti = shang ** 2
            sum_geti += geti
            if yushu == n:
                break
            i += 1
        return sum_geti

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        baocun_set = set()
        baocun_set.add(n)
        while n != 1:
            n = self.get_sum_geti(n)
            if n in baocun_set:
                return False
            else:
                baocun_set.add(n)
        return True

solution = Solution()
solution.isHappy(204)
