a = "345"
b = reversed(a)
print("".join(b))

import functools
def contact_nums(num_str_list):
    """
    :param nums_str: 原来的数
    :return: 拼接成的最大的数
    """
    # 先将每个字符进行翻转
    new_num_str_list = []
    for num_str in num_str_list:
        split_num = int("".join(reversed(num_str)))
        if split_num >= int(num_str):
            new_num_str_list.append(str(split_num))
        else:
            new_num_str_list.append(num_str)

    # 然后进行排序
    def cmp(a, b):
        if a + b > b + a:
            return 1
        elif a + b < b + a:
            return -1
        else:
            return -1
    sort_result = sorted(new_num_str_list, key=functools.cmp_to_key(cmp), reverse=True)
    return "".join(sort_result) if sort_result[0] != "0" else "0"


ans = contact_nums(["4321", "34560"])
print(ans)
