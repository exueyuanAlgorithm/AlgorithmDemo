# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_head_k(self, head, k):
        if head and not head.next and k != 1:
            return head, head, None, False
        if k == 1:
            return head, head, head.next, True
        current = head
        next = current.next
        new_head, new_tail, next_head, is_reverse = self.reverse_head_k(next, k - 1)
        if is_reverse:
            new_tail.next = current
            current.next = None
            return new_head, current, next_head, True
        else:
            current.next = new_head
            return current, new_tail, next_head, False

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        # 需要返回头部的，头指针，尾指针，还有剩余头指针, 是否发生了翻转
        new_head, new_tail, next_head, is_reverse = self.reverse_head_k(head, k)
        next_head = self.reverseKGroup(next_head, k)
        new_tail.next = next_head
        return new_head
