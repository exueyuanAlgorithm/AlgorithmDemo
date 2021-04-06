
def func(s):
    """
    :type s: str
    :rtype: int
    """
    is_read_kongge = False
    is_read_fuhao = False
    is_read_num = False
    read_str = ""
    for item in s:
        if item == " ":
            if is_read_kongge:
                break
        elif item in "-+":
            if is_read_fuhao:
                break
            read_str += item
            is_read_kongge = True
            is_read_fuhao = True
        elif "0" <= item <= "9":
            is_read_kongge = True
            is_read_fuhao = True
            is_read_num = True
            read_str += item
        else:
            break
    if not read_str or not is_read_num:
        return 0
    # print(read_str)
    result = int(read_str)
    if result < - pow(2, 31):
        return - pow(2, 31)
    if result > pow(2, 31) - 1:
        return pow(2, 31) - 1
    return result


print(func("+-12"))

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_read_kongge = False
        is_read_fuhao = False
        is_read_num = False
        read_str = ""
        for item in s:
            if item == " ":
                if is_read_kongge:
                    break
            elif item in "-+":
                if is_read_fuhao:
                    break
                read_str += item
                is_read_kongge = True
                is_read_fuhao = True
            elif "0" <= item <= "9":
                is_read_kongge = True
                is_read_fuhao = True
                is_read_num = True
                read_str += item
            else:
                break
        if not read_str or not is_read_num:
            return 0
        # print(read_str)
        result = int(read_str)
        if result < - pow(2, 31):
            return - pow(2, 31)
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return result