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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        daoshu = head
        qianjin = head
        num = 0
        while qianjin:
            # print("前进:{}".format(qianjin.val))
            # print("倒数:{}".format(daoshu.val))
            num += 1
            if num > n + 1:
                daoshu = daoshu.next
            qianjin = qianjin.next
        if num == n:
            head = head.next
        else:
            daoshu.next = daoshu.next.next
        return head


head = list_to_list_node([1, 2])
solution = Solution()
result = solution.removeNthFromEnd(head, 1)
print(list_node_to_list(result))




