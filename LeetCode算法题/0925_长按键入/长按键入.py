class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_length = len(name)
        typed_length = len(typed)
        if typed_length < name_length:
            return False
        i = 0
        j = 0
        last_letter = ""
        while i < name_length:
            name_letter = name[i]
            if j < typed_length:
                typed_letter = typed[j]
                while typed_letter != name_letter:
                    if typed_letter != last_letter:
                        return False
                    j += 1
                    typed_letter = typed[j]
                else:
                    j += 1
            else:
                return False
            print(name_letter)
            last_letter = name_letter
            i += 1


solution = Solution()
print(solution.isLongPressedName("alex", "aaalex"))
