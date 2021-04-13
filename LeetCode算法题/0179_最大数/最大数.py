import functools

class Solution(object):
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        """
        :type nums: List[int]
        :rtype: str
        """
        def func(num1:str, num2:str):
            while (num1.startswith(num2) or num2.startswith(num1)) and num1 != num2:
                if num1.startswith(num2):
                    num1 = num1[len(num2):]
                else:
                    num2 = num2[len(num1):]
            if num1 < num2:
                return 1
            elif num1 > num2:
                return -1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(func))
        result = "".join(nums)
        i = 0
        while True:
            if i < len(result):
                if result[i] == "0":
                    result = result[1:]
                else:
                    break
            else:
                break
        if not result:
            return "0"
        return result

solution = Solution()
print(solution.largestNumber([0, 0, 0]))