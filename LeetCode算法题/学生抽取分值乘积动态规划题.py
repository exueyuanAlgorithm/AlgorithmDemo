"""
有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

输入描述:
   每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。
输出描述:
输出一行表示最大的乘积。
"""
import copy
from functools import reduce


def qiujie(n: int, scoreList: list, k: int, d: int):
    """
    :param n: 学生数目 1..50
    :param scoreList: 能力值列表 [-50, 20, 30, -20]
    :param k: 选出k个学生
    :param d: 位置编号最大值
    :return:
    """
    maxMutiPlex = None
    maxChoicePositionList = None
    maxChoiceScoreList = None
    for choicePositionList, choiceScoreList in choiceOneList(n, k, d, scoreList, [], [], 0):
        mutiPly = reduce(lambda x, y: x * y, choiceScoreList)
        if maxMutiPlex is None:
            maxMutiPlex = mutiPly
            maxChoicePositionList = choicePositionList
            maxChoiceScoreList = choiceScoreList
        else:
            if mutiPly > maxMutiPlex:
                maxMutiPlex = mutiPly
                maxChoicePositionList = choicePositionList
                maxChoiceScoreList = choiceScoreList
    if maxMutiPlex is not None:
        print("乘积最大的是:{}, 分数分别为:{}, 位置坐标为:{}".format(maxMutiPlex, maxChoiceScoreList, maxChoicePositionList))
    else:
        print("没有符合条件的数据！")


def choiceOneList(n, k, d, scoreList, alreadyChoiceScoreList, alreadyChoicePositionList, deep):
    """
    :param n: n个数
    :param k: 选k个数
    :param d: 差值为d
    :param scoreList: 分值
    :param alreadyChoiceScoreList: 已经选择的数
    :param alreadyChoicePositionList: 已经选择的数的位置
    :return:
    """
    if len(alreadyChoiceScoreList) == k:
        yield alreadyChoicePositionList, alreadyChoiceScoreList
    if alreadyChoicePositionList:
        lastChoicePosition = alreadyChoicePositionList[-1]
        endRange = lastChoicePosition + d
        for nextChoicePosition in range(lastChoicePosition + 1, endRange + 1):
            if nextChoicePosition < len(scoreList):
                alreadyChoicePositionList_new = copy.deepcopy(alreadyChoicePositionList)
                alreadyChoiceScoreList_new = copy.deepcopy(alreadyChoiceScoreList)
                # print("位置坐标:{},已经存在的数据:{},深度:{}".format(nextChoicePosition, alreadyChoicePositionList, deep))
                nextScore = scoreList[nextChoicePosition]
                # print("下一个分数:{}".format(nextScore))
                alreadyChoicePositionList_new.append(nextChoicePosition)
                alreadyChoiceScoreList_new.append(nextScore)
                if len(alreadyChoicePositionList_new) == k:
                    yield alreadyChoicePositionList_new, alreadyChoiceScoreList_new
                else:
                    for choicePositionList, choiceScoreList in choiceOneList(n, k, d, scoreList,
                                                                             alreadyChoiceScoreList_new,
                                                                             alreadyChoicePositionList_new, deep + 1):
                        yield choicePositionList, choiceScoreList
    else:
        for firstChoicePosition, firstScore in enumerate(scoreList):
            # print("第一个位置:%d" % (firstChoicePosition))
            alreadyChoiceScoreList = []
            alreadyChoicePositionList = []
            alreadyChoiceScoreList.append(firstScore)
            alreadyChoicePositionList.append(firstChoicePosition)
            for choicePositionList, choiceScoreList in choiceOneList(n, k, d, scoreList, alreadyChoiceScoreList,
                                                                     alreadyChoicePositionList, deep + 1):
                yield choicePositionList, choiceScoreList


qiujie(10, [10, -20, 25, -30, 45, 7, -30, 45, 80, -22], 3, 2)
