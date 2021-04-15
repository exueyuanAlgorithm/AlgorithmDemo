class Solution(object):
    def halffind(self, search_list, num, low, high):
        mid = (low + high) // 2
        if num == search_list[mid]:
            for i in range(mid + 1, len(search_list)):
                if search_list[i] == search_list[mid]:
                    mid = i
            return mid
        elif low > high:
            return mid

        elif num > search_list[mid]:
            return self.halffind(search_list, num, low + 1, high)
        else:
            return self.halffind(search_list, num, low, high - 1)

    def breakfastNumber(self, new_staple, new_drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        len_staple = len(new_staple)
        len_drinks = len(new_drinks)
        new_staple.sort()
        new_drinks.sort()

        if len_staple < len_drinks:
            bianli_list = new_staple
            search_list = new_drinks
        else:
            bianli_list = new_drinks
            search_list = new_staple

        zongshu = 0
        for item in bianli_list:
            if item >= x:
                break
            shengyu_item = x - item
            weizhi = self.halffind(search_list, shengyu_item, 0, len(search_list) - 1)
            zongshu += weizhi + 1
        return zongshu % (10 ** 9 + 7)


solution = Solution()
# print(solution.halffind([1, 3, 3, 5, 5, 5, 8, 11], 18, 0, 7))
solution.breakfastNumber([3, 8, 7, 6, 9], [4, 6, 8, 7, 4], 10)