
def func(s):
    max_length = 0
    max_chuan = ""
    for position, item in enumerate(s):
        length = 1
        chuan = item
        left_position = position - 1
        right_position = position + 1
        while left_position >= 0 and right_position < len(s):
            left_item = s[left_position]
            right_item = s[right_position]
            if left_item == right_item:
                length += 2
                chuan = left_item + chuan + right_item
                left_position -= 1
                right_position += 1
            else:
                break
        if length > max_length:
            max_length = length
            max_chuan = chuan

        length = 0
        chuan = ""
        left_position = position
        right_position = position + 1
        while left_position >= 0 and right_position < len(s):
            left_item = s[left_position]
            right_item = s[right_position]
            if left_item == right_item:
                length += 2
                chuan = left_item + chuan + right_item
                left_position -= 1
                right_position += 1
            else:
                break
        if length > max_length:
            max_length = length
            max_chuan = chuan
    return max_chuan


print(func("ac"))


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_chuan = ""
        for position, item in enumerate(s):
            length = 1
            chuan = item
            left_position = position - 1
            right_position = position + 1
            while left_position >= 0 and right_position < len(s):
                left_item = s[left_position]
                right_item = s[right_position]
                if left_item == right_item:
                    length += 2
                    chuan = left_item + chuan + right_item
                    left_position -= 1
                    right_position += 1
                else:
                    break
            if length > max_length:
                max_length = length
                max_chuan = chuan

            length = 0
            chuan = ""
            left_position = position
            right_position = position + 1
            while left_position >= 0 and right_position < len(s):
                left_item = s[left_position]
                right_item = s[right_position]
                if left_item == right_item:
                    length += 2
                    chuan = left_item + chuan + right_item
                    left_position -= 1
                    right_position += 1
                else:
                    break
            if length > max_length:
                max_length = length
                max_chuan = chuan
        return max_chuan