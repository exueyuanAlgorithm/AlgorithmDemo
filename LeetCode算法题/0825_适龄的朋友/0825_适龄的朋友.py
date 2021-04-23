import bisect


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        all_num = 0
        for position, age_a in enumerate(ages):
            jiexian_dayu = age_a // 2 + 7
            jiexian2_xiaoyu_dengyu = age_a
            jiexian_xiaoyu_dengyu = jiexian2_xiaoyu_dengyu
            if age_a < 100:
                jiexian3_xiaoyu_dengyu = 100
                jiexian_xiaoyu_dengyu = min(jiexian2_xiaoyu_dengyu, jiexian3_xiaoyu_dengyu)
            if jiexian_xiaoyu_dengyu > jiexian_dayu:
                dayu = bisect.bisect(ages, jiexian_dayu)
                xiaoyudengyu = bisect.bisect(ages, jiexian_xiaoyu_dengyu)
                if xiaoyudengyu >= dayu:
                    all_num += xiaoyudengyu - dayu
                    if dayu <= position <= xiaoyudengyu:
                        all_num -= 1
        return all_num


a = [3, 5, 5, 7, 9, 11]

print(bisect.bisect(a, 4))
print(bisect.bisect(a, 9))
