class Solution:
    def reverseBits(self, n: int) -> int:
        result_num = 0
        for i in range(31):
            if n % 2 == 1:
                result_num = result_num + 1 << 1
            else:
                result_num = result_num << 1
            n = n >> 1
        if n % 2 == 1:
            result_num += 1
        return result_num

solution = Solution()
print(solution.reverseBits(0b111))