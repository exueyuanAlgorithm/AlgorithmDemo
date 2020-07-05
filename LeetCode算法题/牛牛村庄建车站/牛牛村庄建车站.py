
class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def chaStationNum(self, cha):
        if cha == 1:
            return 0
        if self.isPrime(cha):
            return 0
        if cha % 2 == 0:
            return 1
        if self.isPrime(cha-2):
            return 1
        return 2

    def work(self, n, a):
        if n == 1:
            return 1
        else:
            allStationNum = n
            for i, item in enumerate(a[:-1]):
                cha = a[i+1] - a[i]
                allStationNum += self.chaStationNum(cha)
            return allStationNum


solution = Solution()
print(solution.work(3, [0, 7, 11]))