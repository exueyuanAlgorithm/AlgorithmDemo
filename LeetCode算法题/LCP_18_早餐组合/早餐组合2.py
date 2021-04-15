class Solution:
    def breakfastNumber(self, staple, drinks, x: int) -> int:
        staple.sort()
        drinks.sort()
        L = len(drinks)
        cnt = 0
        # 尾指针偏移量
        j = 0
        for i in range(len(staple)):
            if staple[i] >= x:
                break
            while j < L and staple[i] + drinks[L - 1 - j] > x:
                j += 1
            if j >= L:
                break
            cnt += L - j
        return cnt % (pow(10, 9) + 7)
