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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current = head
        if head.next:
            head = head.next
        last = None
        while current:
            temp = current.next
            if temp:
                current.next = temp.next
                temp.next = current
                if last:
                    last.next = temp
                last = current
                current = current.next
            else:
                break
        return head

list_node = list_to_list_node([1, 3])
solution = Solution()
result = solution.swapPairs(list_node)
print(list_node_to_list(result))

