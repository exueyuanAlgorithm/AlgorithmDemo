def bubbleSort(datas: list):
    dataLen = len(datas)
    for i in range(dataLen - 1):
        for j in range(dataLen - 1 - i):
            if datas[j] > datas[j + 1]:
                datas[j], datas[j + 1] = datas[j + 1], datas[j]
    return datas


datas = bubbleSort([2, 3, 1, 5, 8, 7])

print(datas)
