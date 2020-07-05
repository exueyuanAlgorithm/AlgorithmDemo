def gongyueshu(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def gongbeishu(a, b):
    return a * b // gongyueshu(a, b)


print(gongbeishu(100, 25))
