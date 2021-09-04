def IsBracketsValid(sInput):
    input_dict = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []
    for item in sInput:
        if item == "{":
            if stack and stack[-1] in "[(":
                return False
            stack.append("{")
        elif item == "[":
            if stack and stack[-1] == "(":
                return False
            stack.append("[")
        elif item == "(":
            stack.append("(")
        elif item in "}])":
            left_item = input_dict[item]
            if not stack:
                return False
            if stack[-1] != left_item:
                return False
            stack.pop()
    if stack:
        return False
    return True


import random


def rand35():
    return random.randint(1, 35)


def rand47():
    ret = 0
    for _ in range(47):
        ret += rand35()
    return (ret - 1) // 35 + 1

for i in range(1000):
    print(rand47())

# print(IsBracketsValid("{[[()()()]]}"))
