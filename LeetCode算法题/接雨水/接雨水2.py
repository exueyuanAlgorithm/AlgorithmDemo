def get_rain(l):
    # 找出最大值
    l_max = max(l)
    count = 0  # 雨水累加值

    # 寻找列表第一个不低于i和最后一个不低于i的位置，放入l1
    for i in range(1, l_max + 1):
        l1 = []
        for index, value in enumerate(l):
            if value >= i:
                l1.append(index)
        l_exp = l[l1[0]:l1[-1] + 1]
        print(l_exp)
        # 凡是列表中低于i的位置都可以积水
        for ii in l_exp:
            if ii < i:
                count = count + 1
                print('i', i, 'count', count)
    return count

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        # 找出最大值
        l_max = max(height)
        count = 0  # 雨水累加值

        # 寻找列表第一个不低于i和最后一个不低于i的位置，放入l1
        for i in range(1, l_max + 1):
            l1 = []
            for index, value in enumerate(height):
                if value >= i:
                    l1.append(index)
            l_exp = height[l1[0]:l1[-1] + 1]
            print(l_exp)
            # 凡是列表中低于i的位置都可以积水
            for ii in l_exp:
                if ii < i:
                    count = count + 1
                    print('i', i, 'count', count)
        return count


l = [0,1,0,2,1,0,1,3,1,1,2,1]
print(get_rain(l))