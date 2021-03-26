class Solution(object):

    def juhe_qujian(self, lt_num_list, lt_num, left_equal):
        if left_equal:
            last_lt_num = lt_num_list.pop()
            lt_num_list.append([last_lt_num[0], lt_num[1]])
        else:
            is_add = False
            for lt_num_2 in lt_num_list:
                if lt_num[0] <= lt_num_2[0] and lt_num[1] >= lt_num_2[1]:
                    lt_num_2[0] = lt_num[0]
                    lt_num_2[1] = lt_num[1]
                    is_add = True
                    break
            if not is_add:
                lt_num_list.append(lt_num)
    def find132pattern(self, nums):
        lt_num_list = []
        left_equal = False
        for i, num1 in enumerate(nums):
            for lt_num in lt_num_list:
                if lt_num[0] < num1 < lt_num[1]:
                    return True

            if i == len(nums) - 1:
                return False
            num2 = nums[i + 1]
            # print(num1, num2)
            if num1 < num2:
                # 存储num1，num2
                self.juhe_qujian(lt_num_list, [num1, num2], left_equal)
                left_equal = True
                # print(lt_num_list)
            elif num1 > num2:
                left_equal = False

solution = Solution()
print(solution.find132pattern([-1,2, 2,-4,-3, 2]))
