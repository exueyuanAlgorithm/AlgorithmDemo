class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums_set = set()
        count = 0
        i = 1
        while True:
            if i == 1:
                nums_set.add(i)
                count += 1
            elif i % 2 == 0:
                if i // 2 in nums_set:
                    nums_set.add(i)
                    count += 1
            elif i % 3 == 0:
                if i // 3 in nums_set:
                    nums_set.add(i)
                    count += 1
            elif i % 5 == 0:
                if i // 5 in nums_set:
                    nums_set.add(i)
                    count += 1
            if count == n:
                return i
            i += 1


solution = Solution()
print(solution.nthUglyNumber(478))