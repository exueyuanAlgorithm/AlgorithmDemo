def get_max_huiwen(s):
    s_len = len(s)
    dp = [[False for _ in range(s_len)] for _ in range(s_len)]
    max_len = 0
    result = ""
    for k in range(s_len):
        for i in range(s_len):
            j = i + k
            if j >= s_len:
                break
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                    len_ = j - i + 1
                    if len_ > max_len:
                        max_len = len_
                        result = s[i:j+1]
                else:
                    if dp[i + 1][j - 1]:
                        dp[i][j] = True
                        len_ = j - i + 1
                        if len_ > max_len:
                            max_len = len_
                            result = s[i:j + 1]
    return result

print(get_max_huiwen("asasdfgfdsaa"))
