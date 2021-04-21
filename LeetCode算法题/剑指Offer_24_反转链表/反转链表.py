class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        next_node = head.next
        new_head = self.reverseList(next_node)
        next_node.next = head
        head.next = None
        return new_head