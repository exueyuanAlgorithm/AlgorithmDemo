class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        zimu_dict = {}
        left = 0
        max_num = 0
        for right, zimu in enumerate(s):
            zimu_dict[zimu] = zimu_dict.get(zimu, 0) + 1
            max_zimu = max(zimu_dict.values())
            if max_zimu + k < right - left + 1:
                qujian_num = right - left + 1
                if qujian_num > max_num:
                    max_num = qujian_num
            else:
                zimu_dict[s[left]] -= 1
                left += 1
        return max_num
solution = Solution()
print(solution.characterReplacement("AABABBA", 1))
