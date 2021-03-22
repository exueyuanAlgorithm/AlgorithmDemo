
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3_head = None
        l3 = None
        add_num = 0
        while True:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            sum = num1 + num2 + add_num
            gewei = sum % 10
            add_num = sum // 10
            if l3_head is None:
                l3 = ListNode(gewei)
                l3_head = l3
            else:
                l3.next = ListNode(gewei)
                l3 = l3.next
            print(num1, num2, gewei, add_num)
            if (l1 is None or l1.next is None) and (l2 is None or l2.next is None) and add_num == 0:
                break
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return l3_head


l1 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)
l1.next = l11
l11.next = l12

l2 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l2.next = l22
l22.next = l23
solution = Solution()
print(solution.addTwoNumbers(l1, l2))

