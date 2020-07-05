import ListNode
import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, listNode1, listNode2):
        firstListNode = None
        lastListNode = None
        while True:
            if listNode1 is not None and listNode2 is not None:
                if listNode1.val <= listNode2.val:
                    if lastListNode is None:
                        lastListNode = listNode1
                        firstListNode = listNode1
                    else:
                        lastListNode.next = listNode1
                        lastListNode = listNode1
                    listNode1 = listNode1.next
                else:
                    if lastListNode is None:
                        lastListNode = listNode2
                        firstListNode = listNode2
                    else:
                        lastListNode.next = listNode2
                        lastListNode = listNode2
                    listNode2 = listNode2.next
            elif listNode1 is None:
                if lastListNode is None:
                    firstListNode = listNode2
                else:
                    lastListNode.next = listNode2
                return firstListNode
            elif listNode2 is None:
                if lastListNode is None:
                    firstListNode = listNode1
                else:
                    lastListNode.next = listNode1
                return firstListNode

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists

        if len(lists) == 1:
            return lists[0]

        for i in range(math.ceil((math.log2(len(lists))))):
            newLists = []
            if len(lists) % 2 == 0:
                rangeLength = len(lists) // 2
            else:
                rangeLength = len(lists) // 2 + 1
            for i in range(rangeLength):
                position = i*2
                print(position)
                listNode1 = lists[position]
                if position + 1 < len(lists):
                    listNode2 = lists[position + 1]
                    newLists.append(self.mergeTwoLists(listNode1, listNode2))
                else:
                    newLists.append(listNode1)
            lists = newLists
        return lists[0]



def createListNodeList(listNodeListArray):
    """
    :param listNodeListArray:[[1,4,5],[1,3,4],[2,6]]
    :return:
    """
    lists = []
    for listNodeArray in listNodeListArray:
        firstListNode = None
        lastListNode = None
        for i, nodeNum in enumerate(listNodeArray):
            if lastListNode is None:
                listNode = ListNode
                listNode.val = nodeNum
                firstListNode = listNode
                lastListNode = listNode
            else:
                listNode = ListNode
                listNode.val = nodeNum
                lastListNode.next = listNode
                lastListNode = listNode
        lists.append(firstListNode)
    return lists

lists = createListNodeList([])
solution = Solution()
solution.mergeKLists(lists)