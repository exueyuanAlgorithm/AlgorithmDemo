class LinkList(object):
    def __init__(self, ):
        pass

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.capacyDictList = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for position, capacyDict in enumerate(self.capacyDictList):
            if key in capacyDict:
                popDict = self.capacyDictList.pop(position)
                self.capacyDictList.insert(0, popDict)
                return popDict[key]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        insertCapacyDict = {key: value}
        for position, capacyDict in enumerate(self.capacyDictList):
            if key in capacyDict:
                self.capacyDictList.pop(position)
                self.capacyDictList.insert(0, insertCapacyDict)
                return

        if len(self.capacyDictList) < self.capacity:
            self.capacyDictList.insert(0, insertCapacyDict)
        else:
            self.capacyDictList.insert(0, insertCapacyDict)
            self.capacyDictList.pop()

lruCache = LRUCache(2)
lruCache.put(1, 1)
lruCache.put(2, 2)
print(lruCache.get(1))
lruCache.put(3, 3)
print(lruCache.get(2))
lruCache.put(4, 4)
print(lruCache.get(1))
print(lruCache.get(3))
print(lruCache.get(4))
