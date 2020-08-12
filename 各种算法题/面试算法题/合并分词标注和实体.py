
def contactNer(sentence, separateWordList, entityWordList):
    i = 0
    j = 0
    wordPosition = 0
    mergeWordList = []
    while wordPosition < len(sentence):
        separateWordTuple = separateWordList[i]
        entityWordPosition = -1
        entityWordTuple = None
        if j < len(entityWordList):
            entityWordTuple = entityWordList[j]
            entityWordPosition = entityWordTuple[2]
        if wordPosition == entityWordPosition:
            mergeWordList.append(entityWordTuple)
            j += 1
            wordNum = len(entityWordTuple[0])
            separateWordNum = 0
            while separateWordNum != wordNum:
                separateWordNum += len(separateWordList[i][0])
                i += 1
            wordPosition += wordNum
        else:
            mergeWordList.append(separateWordTuple)
            wordPosition += len(separateWordTuple[0])
            i += 1
    return mergeWordList


sentence = "张三通过了北京国美金融有限公司面试"
separateWordList = [("张三", "nr"), ("通过", "v"), ("了","u"), ("北京","ns"), ("国美金融", "nz"), ("有限公司", "n"), ("面试", "n")]
entityWordList = [("张三", "Person", 0), ("北京国美金融有限公司", "Company", 5)]
# mergeWordList = [("张三", "Person"), ("通过", "v"), ("了", "u"), ("北京国美金融有限公司", "Company"), ("面试", "n")]
print(contactNer(sentence, separateWordList, entityWordList))