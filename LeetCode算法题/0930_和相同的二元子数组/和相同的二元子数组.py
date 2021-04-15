
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if not A:
            return 0
        if S == 0:
            return self.numSubarraysZero(A)
        i = 0
        j = 0
        sum = A[i]
        num_sumbary = 0
        while True:
            if j >= len(A):
                break
            if i >= len(A):
                break
            if A[i] == 0:
                i += 1
                continue
            if A[j] == 0:
                j += 1
                sum += 1 if j < len(A) and A[j] == 1 else 0
                continue
            if sum == S:
                num_sumbary += self.calc_num(i, j, A)
                j += 1
                sum += 1 if j < len(A) and A[j] == 1 else 0
                sum -= 1 if A[i] == 1 else 0
                i += 1
            elif sum < S:
                j += 1
                sum += 1 if j < len(A) and A[j] == 1 else 0
                continue
        return num_sumbary

    def calc_num(self, i, j, A):
        zero_num_i = 1
        zero_num_j = 1
        for i_ in range(i - 1, -1, -1):
            if A[i_] == 1:
                break
            else:
                zero_num_i += 1
        for j_ in range(j + 1, len(A)):
            if A[j_] == 1:
                break
            else:
                zero_num_j += 1
        # print(i, j, zero_num_j * zero_num_i)
        return zero_num_i * zero_num_j

    def numSubarraysZero(self, A):
        i = 0
        num_subarray = 0
        while True:
            if i >= len(A):
                break
            if A[i] != 0:
                i += 1
                continue
            zero_count = 0
            is_jieshu = False
            for j in range(i, len(A)):
                if A[j] == 0:
                    zero_count += 1
                else:
                    i = j + 1
                    break
                if j == len(A) - 1:
                    is_jieshu = True
            num_subarray += self.clac_combinary(zero_count)
            if is_jieshu:
                break
        return num_subarray

    def clac_combinary(self, num):
        comb_sum = 0
        for i in range(1, num+1):
            comb_sum += i
        return comb_sum


solution = Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1,0,1], 2))
