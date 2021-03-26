# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        already_have_set = set(head.val)
        last = head
        while last.next:
            current = last.next
            if current.val in already_have_set:
                last.next = current.next
            else:
                already_have_set.add(current.val)
                last = current
        return head

