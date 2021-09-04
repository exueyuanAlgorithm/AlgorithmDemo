import collections


def convert_s_to_t(S, T):
    if S == T:
        return 0
    s_dict = collections.defaultdict(int)
    t_dict = collections.defaultdict(int)
    for item in S:
        s_dict[item] += 1
    for item in T:
        t_dict[item] += 1
    if s_dict != t_dict:
        return -1
    length = len(S)
    i = 0
    j = 0
    count = 0
    while i < length and j < length:
        if S[i] == T[j]:
            i += 1
            j += 1
            count += 1
        else:
            i += 1
    return length - count


if __name__ == "__main__":
    ans = convert_s_to_t("abcde", "edcba")
    print(ans)
