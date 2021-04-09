import copy
class Solution(object):
    def bianhuan(self, dengpao_state_, m, zhuangtai_set):
        if m == 0:
            zhuangtai_set.add(tuple(dengpao_state_))
            return
        for i in range(4):
            dengpao_state = copy.deepcopy(dengpao_state_)
            if i == 0:
                for j, dengpao in enumerate(dengpao_state):
                    dengpao_state[j] = not dengpao_state[j]
                self.bianhuan(dengpao_state, m - 1, zhuangtai_set)
            elif i == 1:
                for j in range(0, len(dengpao_state)//2 + 1):
                    if j*2 < len(dengpao_state):
                        dengpao_state[j*2] = not dengpao_state[j*2]
                self.bianhuan(dengpao_state, m - 1, zhuangtai_set)
            elif i == 2:
                for j in range(0, len(dengpao_state)//2 + 1):
                    if j*2 + 1 < len(dengpao_state):
                        dengpao_state[j*2+1] = not dengpao_state[j*2+1]
                self.bianhuan(dengpao_state, m - 1, zhuangtai_set)
            elif i == 3:
                for j in range(0, len(dengpao_state)//3 + 1):
                    if j*3 < len(dengpao_state):
                        dengpao_state[j*3] = not dengpao_state[j*3]
                self.bianhuan(dengpao_state, m - 1, zhuangtai_set)

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        dengpao_state = [True] * n
        zhuangtai_set = set()
        self.bianhuan(dengpao_state, m, zhuangtai_set)
        return len(zhuangtai_set)

solution = Solution()
print(solution.flipLights(4, 100))

