# 前缀：不包括自己的所有前面的字符串
# 后缀：不包括自己的所有后面的字符串
# 最长前后缀相等序列：

# i：后缀的最后一位的下标
# j：前缀的最后一位的下标
def get_next(p):
    next = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = next[j - 1]
        if p[i] == p[j]:
            j += 1
        next[i] = j
    return next


def KMP(s, p):
    next = get_next(p)
    j = 0
    for i, item in enumerate(s):
        while j > 0 and item != p[j]:
            j = next[j - 1]
        if item == p[j]:
            j += 1
            if j == len(p):
                return i - len(p) + 1
    return -1

print(KMP("aabaabaaf", "aabaaf"))
