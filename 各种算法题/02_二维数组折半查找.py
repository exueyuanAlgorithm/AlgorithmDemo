import numpy as np


def searchNum(datalist, searchdata):
    row, colums = np.shape(datalist)
    if row <= 0 or colums <= 0:
        return False

    firstData = datalist[0, 0]
    lastData = datalist[-1, -1]
    if searchdata < firstData or searchdata > lastData:
        return False

    row_half = row//2
    colums_half = colums//2
    half_data = datalist[row_half, colums_half]
    if searchdata == half_data:
        return True
    datalist1 = None
    datalist2 = None
    if searchdata > half_data:
        datalist1 = datalist[row_half+1:, :]
        datalist2 = datalist[:row_half+1, colums_half+1:]
    elif searchdata < half_data:
        datalist1 = datalist[:row_half,:]
        datalist2 = datalist[row_half:, :colums_half]
    isHave1 = searchNum(datalist1, searchdata)
    if isHave1:
        return True
    else:
        isHave2 = searchNum(datalist2, searchdata)
        return isHave2




datalist = np.array([[1, 2, 3],
                     [3, 5, 8],
                     [4, 6, 12],
                     [7, 12, 17],
                     [11, 18, 25],
                     [12, 28, 39]])

print(searchNum(datalist, 5))
