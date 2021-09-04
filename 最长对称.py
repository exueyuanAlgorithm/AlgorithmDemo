
def longest_odd_huiwen(s):
    s_len = len(s)
    max_length = 0
    result = ""
    for position, item in enumerate(s):
        length = 1
        temp_str = item
        left_position = position -1
        right_position = position + 1
        while left_position >= 0 and right_position < s_len:
            left_item = s[left_position]
            right_item = s[right_position]
            if left_item == right_item:
                length += 2
                temp_str = left_item + temp_str + right_item
                left_position -= 1
                right_position += 1
            else:
                break
        if length > max_length:
            max_length = length
            result = temp_str
    return result