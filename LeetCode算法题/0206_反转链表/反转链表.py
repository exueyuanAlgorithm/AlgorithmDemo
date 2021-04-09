# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_list_node(num_list):
    head = None
    last = None
    for num in num_list:
        list_node = ListNode(num)
        if last:
            last.next = list_node
        last = list_node
        if not head:
            head = last
    return head


def list_node_to_list(head):
    last = head
    num_list = []
    while last:
        num_list.append(last.val)
        last = last.next
    return num_list


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


list_node = list_to_list_node([1, 2, 3, 4, 5])
solution = Solution()
head = solution.reverseList(list_node)

