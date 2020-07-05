
def factoryUpdate(n, m, u, v, q):
    """
    :param n: n个工厂 4
    :param m: m词生产力升级 2
    :param u: u和v关联 [1, 2, 2]
    :param v: u和v关联 [2, 3, 4]
    :param q: 生产力提升的位置 [ 2, 1]
    :return: 生产力提升后，各个位置的生产力[2, 2, 1, 1]
    """
    factoryDict = {}
    for i in range(len(u)):
        uu = u[i]
        vv = v[i]
        factoryList1 = factoryDict.get(uu, [])
        factoryList1.append(vv)
        factoryDict[uu] = factoryList1

        factoryList2 = factoryDict.get(vv, [])
        factoryList2.append(uu)
        factoryDict[vv] = factoryList2
    print(factoryDict)

    productivityList = [0] * n
    for i in range(m):
        factoryNum = q[i]
        productivityList[factoryNum-1] += 1
        factoryList = factoryDict.get(factoryNum, [])
        for factoryNum2 in factoryList:
            productivityList[factoryNum2-1] += 1
    return productivityList


print(factoryUpdate(4, 2, [1, 2, 2], [2, 3, 4], [2, 1]))