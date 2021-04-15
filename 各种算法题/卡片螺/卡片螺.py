class Solution(object):
    def __init__(self, n, m):
        self.kapianluo_list = [[j] for j in range(n)]

    def handle(self, xuhao, x, y):
        if xuhao == 1:
            num = self.kapianluo_list[x-1].pop()
            self.kapianluo_list[y-1].append(num)
            return num
        elif xuhao == 2:
            return self.kapianluo_list[x-1][y-1]

solution = Solution(5, 20)
solution.handle(1, 1, 5)
print(solution.handle(2, 5, 1))
