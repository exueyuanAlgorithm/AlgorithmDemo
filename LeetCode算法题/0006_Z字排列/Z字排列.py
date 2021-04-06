
def func(s, z):
    if z == 1:
        return s
    lunhui = (z - 1) * 2
    str_list = [""] * z
    for position, item in enumerate(s):
        for hangshu in range(z):
            if position % lunhui == hangshu or position % lunhui == lunhui - hangshu:
                str_list[hangshu] += item
    result = "".join(str_list)

        #
        #
        # if position % lunhui == 0:
        #     # print(item)
        #     pass
        # if position % lunhui == 1 or position % lunhui == lunhui - 1:
        #     # print(item)
        #     pass
        # if position % lunhui == 2 or position % lunhui == lunhui -2:
        #     # print(item)
        #     pass
        # if position % lunhui == 3 or position % lunhui == lunhui -3:
        #     print(item)


    return result






print(func("paypalishiring", 1))