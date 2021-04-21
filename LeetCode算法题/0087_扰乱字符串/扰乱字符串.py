class Solution(object):
    def isScramble_dict(self, s1, s2, scram_dict):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 判断 s1 和 s2
        if s1 == s2:
            scram_dict[(s1, s2)] = True
            return True
        if len(s1) == 1:
            scram_dict[(s1, s2)] = False
            return False
        # 遍历s1
        s1_dict = {}
        for item in s1:
            s1_dict[item] = s1_dict.get(item, 0) + 1
        s2_dict = {}
        for item in s2:
            s2_dict[item] = s2_dict.get(item, 0) + 1

        if s1_dict != s2_dict:
            scram_dict[(s1, s2)] = False
            return False

        for i in range(1, len(s1)):
            s1_left = s1[:i]
            s1_right = s1[i:]
            s2_left = s2[:i]
            s2_right = s2[i:]
            # 比较
            if (s1_left, s2_left) in scram_dict:
                bijiao1 = scram_dict[(s1_left, s2_left)]
            else:
                bijiao1 = self.isScramble_dict(s1_left, s2_left, scram_dict)

            if (s1_right, s2_right) in scram_dict:
                bijiao2 = scram_dict[(s1_right, s2_right)]
            else:
                bijiao2 = self.isScramble_dict(s1_right, s2_right, scram_dict)
            if bijiao1 and bijiao2:
                scram_dict[(s1, s2)] = True
                return True

            s2_left_2 = s2[-i:]
            s2_right_2 = s2[:-i]
            if (s1_left, s2_left_2) in scram_dict:
                bijiao1 = scram_dict[(s1_left, s2_left_2)]
            else:
                bijiao1 = self.isScramble_dict(s1_left, s2_left_2, scram_dict)

            if (s1_right, s2_right_2) in scram_dict:
                bijiao2 = scram_dict[(s1_right, s2_right_2)]
            else:
                bijiao2 = self.isScramble_dict(s1_right, s2_right_2, scram_dict)
            if bijiao1 and bijiao2:
                scram_dict[(s1, s2)] = True
                return True
        scram_dict[(s1, s2)] = False
        return False

    def isScramble(self, s1, s2):
        return self.isScramble_dict(s1, s2, {})

solution = Solution()
x1 = "eebaacbcbcadaaedceaaacadccd"
x2 = "eadcaacabaddaceacbceaabeccd"
print(solution.isScramble(x1, x2))