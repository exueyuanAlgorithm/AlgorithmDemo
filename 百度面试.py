import collections
def left_side_view(root):
    if not root:
        return []
    my_deque = collections.deque()
    my_deque.append((root, 0))
    now_layer_num = -1
    result_list = []
    while my_deque:
        node, layer_num = my_deque.popleft()
        if layer_num != now_layer_num:
            result_list.append(node.val)
            now_layer_num = layer_num
        if node.left:
            my_deque.append((node.left, layer_num + 1))
        if node.right:
            my_deque.append((node.right, layer_num + 1))
    return result_list

def longest_huiwen_sub_str(s):
    s_len = len(s)
    dp = [[False] * s_len for _ in range(s_len)]
    max_length = 0
    result = ""
    for k in range(s_len):
        for i in range(s_len):
            j = i + k
            if j >= s_len:
                break
            if j - i <= 1:
                if s[i] == s[j]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        result = s[i:j+1]
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        result = s[i:j+1]
    return result

result = longest_huiwen_sub_str("acabad")
print(result)
