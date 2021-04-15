import math


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        num_dict = {}
        for num in deck:
            num_dict[num] = num_dict.get(num, 0) + 1
        all_zhiyinshu_set = None
        for key, value in num_dict.items():
            zhiyinshu_set = set()
            if value == 1:
                return False
            for i in range(1, int(math.sqrt(value)) + 1):
                if value % i == 0:
                    j = value // i
                    if i != 1:
                        zhiyinshu_set.add(i)
                    if j != 1:
                        zhiyinshu_set.add(j)
            if all_zhiyinshu_set is not None:
                all_zhiyinshu_set = all_zhiyinshu_set & zhiyinshu_set
            else:
                all_zhiyinshu_set = zhiyinshu_set
        if all_zhiyinshu_set:
            return True
        else:
            return False


solution = Solution()
print(solution.hasGroupsSizeX([1,1,2,2,2,3,3,3,3,3,3]))
