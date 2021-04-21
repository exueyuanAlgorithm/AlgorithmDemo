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

    def combinationSum_3(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # print(candidates, target)
        if not candidates:
            return []
        candidates.sort()
        large_position = self.halffind(candidates, target, 0, len(candidates) - 1)
        candidates = candidates[:large_position + 1]
        if not candidates:
            return []
        if sum(candidates) < target:
            return []
        all_zuhe_list = []
        for position, xuanze_num in enumerate(candidates):
            if target == xuanze_num:
                all_zuhe_list.append([xuanze_num])
            new_candidates = candidates[:position] + candidates[position+1:]
            zuhe_list = self.combinationSum2(new_candidates, target - xuanze_num)
            for zuhe in zuhe_list:
                zuhe.append(xuanze_num)
                zuhe.sort()
                all_zuhe_list.append(zuhe)
        return all_zuhe_list

    def combinationSum2(self, candidates, target):
        all_zuhe_list = self.combinationSum_3(candidates, target)
        new_zuhe_set = set()
        for zuhe in all_zuhe_list:
            zuhe.sort()
            new_zuhe_set.add(tuple(zuhe))
        result_list = []
        for zuhe in new_zuhe_set:
            result_list.append(list(zuhe))
        return result_list

        # print(candidates)
        # print(large_position)


solution = Solution()

print(solution.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
# print(solution.halffind([2, 3, 6, 9], 1, 0, 3))
