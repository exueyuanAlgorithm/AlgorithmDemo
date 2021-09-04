import copy
def max_buid(n, restrictions):
    temp_restrict = copy.deepcopy(restrictions)
    temp_restrict.append([1, 0])
    temp_restrict.sort()
    

    m = len(temp_restrict)
    for i in range(1, m):
        temp_restrict[i][1] = min(temp_restrict[i][1], temp_restrict[i-1][1] + temp_restrict[i][0] - temp_restrict[i-1][0])

    for i in range(m-2, -1, -1):
        temp_restrict[i][1] = min(temp_restrict[i][1], temp_restrict[i+1][1] + temp_restrict[i+1][0] - temp_restrict[i][0])
    result = 0
    for i in range(m):
        result = max(result, temp_restrict[i+1][0] - temp_restrict[i][0] + temp_restrict[i][1] + temp_restrict[i+1][1])
    return result
