class Solution(object):

    # def juhe_qujian(self, ):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lt_num_list = []
        left_equal = False

        for i, num1 in enumerate(nums):
            for lt_num in lt_num_list:
                if lt_num[2]:
                    if lt_num[0] <= num1 < lt_num[1]:
                        return True
                else:
                    if lt_num[0] < num1 < lt_num[1]:
                        return True

            if i == len(nums) - 1:
                return False
            num2 = nums[i + 1]
            # print(num1, num2)
            if num1 < num2:
                # 存储num1，num2
                lt_num_list.append([num1, num2, left_equal])
                left_equal = True
                # print(lt_num_list)
            elif num1 > num2:
                left_equal = False

solution = Solution()
print(solution.find132pattern([-1,2, 2,0,3, 2]))
