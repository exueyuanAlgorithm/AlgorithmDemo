
# import collections
# def get_max_with(node):
#     if not node:
#         return 0
#     my_deque = collections.deque()
#     my_deque.append((node, 0))
#     cur_pos = 0
#     result = 0
#     cur_num = 0
#     while my_deque:
#         node_, pos = my_deque.popleft()
#         if pos == cur_pos:
#             cur_num += 1
#         else:
#             result = max(result, cur_num)
#             cur_pos = pos
#             cur_num = 1
#         if node_.left:
#             my_deque.append((node_.left, pos + 1))
#         if node_.right:
#             my_deque.append((node_.right, pos + 1))
#     result = max(result, cur_num)
#     return result

class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        stack = []
        now_length = 0
        result = 0
        for i, item in enumerate(s):
            if item == "(":
                stack.append([item, now_length])
                now_length = 0
            elif item == ")":
                if stack and stack[-1][0] == "(":
                    now_length = stack[-1][1] + 2 + now_length
                    result = max(now_length, result)
                    stack.pop()
                else:
                    now_length = 0
        return result
solution = Solution()
ans = solution.longestValidParentheses("()(())")
print(ans)