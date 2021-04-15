class Solution:
    def breakfastNumber(self, staple, drinks, x: int) -> int:
        staple.sort()
        drinks.sort()
        len_drinks = len(drinks)
        count = 0
        j = len_drinks - 1
        for i in range(len(staple)):
            if staple[i] >= x:
                break
            while j >= 0 and staple[i] + drinks[j] > x:
                j -= 1
            if j < 0:
                break
            count += j + 1
        return count % (pow(10, 9) + 7)

solution = Solution()
staple = [7,3,4,3,9,9,10,8,8,3]
drinks = [7,10,6,7,5,2,8,4,5,8]
x = 5
solution.breakfastNumber(staple, drinks, x)