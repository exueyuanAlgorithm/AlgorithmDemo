def get_next_array(p):
    next_array = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = next_array[j - 1]
        if p[j] == p[i]:
            j += 1
        next_array[i] = j
    return next_array


def kmp(s, p):
    next_array = get_next_array(p)
    j = 0
    for i, item in enumerate(s):
        while j > 0 and item != p[j]:
            j = next_array[j - 1]
        if item == p[j]:
            j += 1
            if j == len(p):
                return i - len(p) + 1
    return -1
# for i in range(1, len(s)):
#     while j > 0 and next_array[i] != next_array[j]
