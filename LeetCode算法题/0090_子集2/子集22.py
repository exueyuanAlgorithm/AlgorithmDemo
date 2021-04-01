import copy


class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_num_set = set()
        list_num_set.add(tuple())
        for num in nums:
            set_2 = set()
            for list_num_tuple in list_num_set:
                num_list = [num]
                num_list.extend(list_num_tuple)
                num_list.sort()
                set_2.add(tuple(num_list))
            list_num_set = list_num_set | set_2
        result_list = []
        for list_num_tuple in list_num_set:
            item = list(list_num_tuple)
            result_list.append(item)
        return result_list


solution = Solution()
result = solution.subsetsWithDup([3, 2, 2, 2, 5, 3])
print(result)
