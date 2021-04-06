def func(num):
    if num < 0:
        return False
    i = 1
    num_list = []
    while True:
        if num // pow(10, i) > 0:
            yushu = num % pow(10, i)
            yushu = yushu // pow(10, i - 1)
            i += 1
            num_list.append(yushu)
        else:
            break
    yushu = num // pow(10, i - 1)
    num_list.append(yushu)
    i = 0
    j = len(num_list) - 1
    while i < j:
        if num_list[i] == num_list[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num < 0:
            return False
        i = 1
        num_list = []
        while True:
            if num // pow(10, i) > 0:
                yushu = num % pow(10, i)
                yushu = yushu // pow(10, i - 1)
                i += 1
                num_list.append(yushu)
            else:
                break
        yushu = num // pow(10, i - 1)
        num_list.append(yushu)
        i = 0
        j = len(num_list) - 1
        while i < j:
            if num_list[i] == num_list[j]:
                i += 1
                j -= 1
            else:
                return False
        return True



print(func(4848))
