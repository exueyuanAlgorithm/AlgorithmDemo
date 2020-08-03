
def countSort(teacherScoreList, studentScoreList):
    teacherScoreSort = [0] * 10
    studentScoreSort = [0] * 10
    for i in range(len(teacherScoreList)):
        teacherScore, studentScore = teacherScoreList[i], studentScoreList[i]
        teacherScoreSort[teacherScore - 1] += 1
        studentScoreSort[studentScore - 1] += 1
    i = 0
    j = 0
    matchList = []
    allScore = 0
    while len(matchList) < len(teacherScoreList):
        teacherScore = -1
        studentScore = -1
        while teacherScoreSort[i] == 0:
            i += 1
        else:
            teacherScore = i + 1
            teacherScoreSort[i] -= 1

        while studentScoreSort[j] == 0:
            j += 1
        else:
            studentScore = j + 1
            studentScoreSort[j] -= 1

        if teacherScore != -1 and studentScore != -1:
            allScore += teacherScore * studentScore
            matchList.append((teacherScore, studentScore))
    return matchList, allScore


print(countSort([3, 1, 8, 8, 5, 9], [10, 9, 3, 3, 7, 4]))
