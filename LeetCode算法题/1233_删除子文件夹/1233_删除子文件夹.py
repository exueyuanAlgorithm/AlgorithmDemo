class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        remove_set = set()
        for i in range(len(folder) - 1):
            for j in range(i + 1, len(folder)):
                folder_1 = folder[i]
                folder_2 = folder[j]
                if folder_1.startswith(folder_2 + "/"):
                    remove_set.add(i)
                if folder_2.startswith(folder_1 + "/"):
                    remove_set.add(j)
        for i in range(len(folder) - 1, -1, -1):
            if i in remove_set:
                folder.pop(i)
        return folder
