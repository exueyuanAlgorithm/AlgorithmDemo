import copy
class Solution(object):
    def choice_num(self, nums, size):
        if size > len(nums):
            return [[]]
        if size == 0:
            return [[]]
        # 某个数组中，选择x个
        result_list = []
        for i in range(0, len(nums) - size + 1):
            num = nums[i]
            choice_nums = [num]
            choice_list = self.choice_num(nums[i+1:], size-1)
            # print(nums[i+1:], size-1, choice_list)
            for choice in choice_list:
                choice_nums_2 = copy.deepcopy(choice_nums)
                choice_nums_2.extend(choice)
                if len(choice_nums_2) == size:
                    result_list.append(choice_nums_2)
        return result_list


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_num_set = set()
        for size in range(0, len(nums)+1):
            result = self.choice_num(nums, size)
            for item in result:
                item.sort()
                item_tuple = tuple(item)
                list_num_set.add(item_tuple)
        result_list = []
        for list_num_tuple in list_num_set:
            item = list(list_num_tuple)
            result_list.append(item)
        return result_list



solution = Solution()
result = solution.subsetsWithDup([3,2,2, 2, 5, 3])
print(result)