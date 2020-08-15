
str = "sdkfjksdjf192.168.8.23skdfj2.3.2"

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def matchStr(str):
    matchList = []
    num0 = ""
    numNum = 0
    for position, item in enumerate(str):
        if item in nums:
            num0 += item
            if num0!="" and len(num0) >= 2 and num0[-2] == ".":
                numNum += 1
                if numNum == 3:
                    matchList.append(num0)
        elif item == ".":
            if num0 != "" and num0[-1] != ".":
                num0 += "."
        else:
            num0 = ""
    return matchList
print(matchStr("sdkfjksdjf192.168.8.23skdfj2.3.2"))