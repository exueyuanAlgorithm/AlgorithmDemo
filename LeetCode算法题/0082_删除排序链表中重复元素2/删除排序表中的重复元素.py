
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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


class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return head
        head_num = head.val
        while head and head.next and head.next.val == head_num:
            head = head.next.next
            while head and head.val == head_num:
                head = head.next
            if head:
                head_num = head.val


        last = head
        while last:
            if last and last.next and last.next.next and last.next.val == last.next.next.val:
                delete_num = last.next.val
                last.next = last.next.next.next
                while last.next and last.next.val == delete_num:
                    last.next = last.next.next

                if last.next and last.next.next and last.next.val == last.next.next.val:
                    continue
            last = last.next
        return head


head = list_to_list_node([1,1,1])

solution = Solution()
head2 = solution.deleteDuplicates(head)

print(list_node_to_list(head2))









