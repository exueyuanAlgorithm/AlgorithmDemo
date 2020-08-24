class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newAddress = ""
        for ad in address:
            if ad == ".":
                newAddress += "[.]"
            else:
                newAddress += ad
        return newAddress