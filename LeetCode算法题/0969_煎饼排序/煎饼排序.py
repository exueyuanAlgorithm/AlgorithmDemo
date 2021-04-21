class Solution(object):
    def pancakeSort(self, arr: list):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length = len(arr)
        num = length
        result_list = []
        while True:
            max_index = None
            max_num = -100000
            for i in range(num):
                num_ = arr[i]
                if num_ > max_num:
                    max_num = num_
                    max_index = i
            if max_index is not None:
                if max_index == num - 1:
                    num -= 1
                    continue
                if max_index == 0:
                    result_list.append(num)
                    new_arr = arr[:num]
                    new_arr.reverse()
                    arr = new_arr + arr[num:]
                    num -= 1
                    continue
                else:
                    result_list.append(max_index + 1)
                    new_arr = arr[:max_index + 1]
                    new_arr.reverse()
                    arr = new_arr + arr[max_index + 1:]

                    result_list.append(num)
                    new_arr = arr[:num]
                    new_arr.reverse()
                    arr = new_arr + arr[num:]
                    num -= 1
                    continue
            else:
                break
        return result_list

solution = Solution()
print(solution.pancakeSort([3, 2, 4, 1]))

