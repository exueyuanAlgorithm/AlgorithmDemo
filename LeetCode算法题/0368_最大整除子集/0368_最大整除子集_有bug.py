class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cache_dict = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                if num1 % num2 == 0 or num2 % num1 == 0:
                    num1_set = cache_dict.get(num1, set())
                    num1_set.add(num2)
                    cache_dict[num1] = num1_set

                    num2_set = cache_dict.get(num2, set())
                    num2_set.add(num1)
                    cache_dict[num2] = num2_set

        sorted_list = sorted(cache_dict.items(), key=lambda item: len(item[1]))
        i = 0
        while True:
            if i >= len(sorted_list):
                break
            sorted_list.sort(key=lambda item: len(item[1]))
            item = sorted_list[i]
            if len(item[1]) < len(sorted_list):
                for shanchuguanlian in item[1]:
                    if shanchuguanlian != item[0]:
                        cache_dict.get(shanchuguanlian, set()).remove(item[0])
                del cache_dict[item[0]]
                # 进行删除
                sorted_list.pop(i)
            else:
                i += 1
        sorted_list[0][1].add(sorted_list[0][0])
        return list(sorted_list[0][1])


solution = Solution()
print(solution.largestDivisibleSubset([3, 4, 6, 8, 12, 16, 32]))
