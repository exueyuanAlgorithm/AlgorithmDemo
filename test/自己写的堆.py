import queue

queue1 = queue.Queue()
queue1.put(3)
queue1.put(4)
queue1.put(5)
queue1.put(5)

print(list(queue1.queue)[-1])
print(queue1.get_nowait())
print(queue1.get_nowait())


# print(queue1.get_nowait())
# print(queue1.get_nowait())

def add_data(result_list, num):
    result_list.append(num)
    position = len(result_list) - 1
    if position == 0:
        return
    parent_position = (position - 1) // 2
    while result_list[parent_position] < result_list[position]:
        temp = result_list[parent_position]
        result_list[parent_position] = result_list[position]
        result_list[position] = temp
        if parent_position == 0:
            break
        position = parent_position
        parent_position = (position - 1) // 2


def replace_data(result_list, num):
    if num >= result_list[0]:
        return

    result_list[0] = num
    position = 0
    while True:
        left_position = position * 2 + 1
        right_position = position * 2 + 2
        if left_position >= len(result_list):
            break
        if result_list[position] >= result_list[left_position] and right_position < len(result_list) and \
                result_list[position] >= result_list[right_position]:
            break
        if result_list[position] < result_list[left_position]:
            temp = result_list[position]
            result_list[position] = result_list[left_position]
            result_list[left_position] = temp
            position = left_position
        elif right_position < len(result_list) and result_list[position] < result_list[right_position]:
            temp = result_list[position]
            result_list[position] = result_list[right_position]
            result_list[right_position] = temp
            position = right_position
        else:
            break


result_list = []
add_data(result_list, 3)
add_data(result_list, 8)
add_data(result_list, 5)
add_data(result_list, 2)
add_data(result_list, 9)
add_data(result_list, 100)
add_data(result_list, -8)
add_data(result_list, 11)
print(result_list)
replace_data(result_list, -8)
replace_data(result_list, 100)
replace_data(result_list, 10)
print(result_list)
