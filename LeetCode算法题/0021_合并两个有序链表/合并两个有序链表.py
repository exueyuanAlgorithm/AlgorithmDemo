# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, listNode1, listNode2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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
