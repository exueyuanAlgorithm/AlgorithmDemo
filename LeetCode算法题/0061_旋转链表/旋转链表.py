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
        print(last.val)
        num_list.append(last.val)
        last = last.next
    return num_list

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        all_num = 0
        current = head
        num_dict = {}
        while current:
            all_num += 1
            num_dict[all_num] = current
            current = current.next
        rotate_num = k % all_num
        right_num = all_num - rotate_num + 1
        if rotate_num == 0:
            return head
        else:
            if right_num - 1 > 0:
                num_dict[right_num-1].next = None
            head2 = num_dict[right_num]
            num_dict[all_num].next = head
        return head2

head = list_to_list_node([])
solution = Solution()
head2 = solution.rotateRight(head, 2)
print(list_node_to_list(head2))




