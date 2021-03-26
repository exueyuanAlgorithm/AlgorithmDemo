class NestedIterator(object):

    def qiantao(self, nestedList, result_list):
        if isinstance(nestedList, int):
            result_list.append(nestedList)
            return
        for item in nestedList:
            self.qiantao(item, result_list)

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.result_list = []
        self.qiantao(nestedList, self.result_list)
        self.num = 0


    def next(self):
        """
        :rtype: int
        """
        result = self.result_list[self.num]
        self.num += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.num < len(self.result_list):
            return True
        else:
            return False

nested_iter = NestedIterator([[3],8,[5,[4,6],[]]])
while(nested_iter.hasNext()):
    print(nested_iter.next())