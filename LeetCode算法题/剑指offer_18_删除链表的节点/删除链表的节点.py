# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        last = head
        while last:
            if last.next and last.next.val == val:
                last.next = last.next.next
                return head
            last = last.next
