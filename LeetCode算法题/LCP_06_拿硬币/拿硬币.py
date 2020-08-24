class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        cishu = 0
        for coin in coins:
            if coin % 2 == 0:
                cishu += coin // 2
            else:
                cishu += coin // 2 + 1
        return cishu