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

def print_list_node(head):
    last = head
    while last:
        print(last.val)
        last = last.next


head = list_to_list_node([3, 2, 5])
print_list_node(head)

# print(head)



