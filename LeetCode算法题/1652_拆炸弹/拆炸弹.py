class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            for i in range(len(code)):
                code[i] = 0
            return code
        if k > 0:
            sum_ = None
            result_list = []
            for i in range(len(code)):
                if sum_ is None:
                    sum_ = 0
                    for j in range(1, 1 + k):
                        sum_ += code[j]
                    result_list.append(sum_)
                else:
                    sum_ -= code[i]
                    if i + k < len(code):
                        sum_ += code[i + k]
                    else:
                        sum_ += code[i + k - len(code)]
                    result_list.append(sum_)
            return result_list
        if k < 0:
            sum_ = None
            result_list = []
            for i in range(len(code)):
                if sum_ is None:
                    sum_ = 0
                    for i in range(-1, k - 1, -1):
                        sum_ += code[i]
                    result_list.append(sum_)
                else:
                    sum_ -= code[i + k - 1]
                    sum_ += code[i - 1]
                    result_list.append(sum_)
            return result_list
