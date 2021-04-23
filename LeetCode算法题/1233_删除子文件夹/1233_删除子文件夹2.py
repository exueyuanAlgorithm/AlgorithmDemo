class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """

        # def func(fold):
        #     count = 0
        #     for item in fold:
        #         if item == "/":
        #             count += 1
        #     return count
        #
        # folder.sort(key=func)

        fold_set = set()
        for fold in folder:
            fold_set.add(fold + "/")
        for i in range(len(folder) - 1, -1, -1):
            fold = folder[i]
            search_fold = fold
            match_chuan = ""
            chuan_position = search_fold.find("/")
            while chuan_position != -1:
                match_chuan += search_fold[:chuan_position + 1]
                if match_chuan in fold_set:
                    folder.pop(i)
                    break
                search_fold = search_fold[chuan_position + 1:]
                chuan_position = search_fold.find("/")
        return folder


solution = Solution()
print(solution.removeSubfolders(["/a/b/c", "/a/b/d", "/b", "/a/b/ca", "/a/b", "/abced/a/b/a/c"]))
