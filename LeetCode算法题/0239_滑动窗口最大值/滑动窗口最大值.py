class LinkNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head_node = LinkNode()
        self.tail_node = LinkNode()
        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node
        self.count = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.count or index < 0:
            return -1
        if index < (self.count + 1) // 2:
            num = 0
            node = self.head_node.next
            while node:
                if index == num:
                    return node.val
                node = node.next
                num += 1
        else:
            reverse_index = self.count - index - 1
            num = 0
            node = self.tail_node.prev
            while node:
                if num == reverse_index:
                    return node.val
                node = node.prev
                num += 1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        add_node = LinkNode(val)
        add_node.next = self.head_node.next
        add_node.prev = self.head_node
        self.head_node.next = add_node
        add_node.next.prev = add_node
        self.count += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        add_node = LinkNode(val)
        add_node.prev = self.tail_node.prev
        add_node.next = self.tail_node
        self.tail_node.prev = add_node
        add_node.prev.next = add_node
        self.count += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.count:
            self.addAtTail(val)
            return
        if index > self.count:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        add_node = LinkNode(val)
        charu_node = None
        if index < (self.count + 1) // 2:
            num = 0
            node = self.head_node.next
            while node:
                if index == num:
                    charu_node = node
                node = node.next
                num += 1
        else:
            reverse_index = self.count - index - 1
            num = 0
            node = self.tail_node.prev
            while node:
                if num == reverse_index:
                    charu_node = node
                node = node.prev
                num += 1
        add_node.next = charu_node
        add_node.prev = charu_node.prev
        charu_node.prev.next = add_node
        charu_node.prev = add_node
        self.count += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.count or index < 0:
            return
        delete_node = None
        if index < (self.count + 1) // 2:
            num = 0
            node = self.head_node.next
            while node:
                if index == num:
                    delete_node = node
                node = node.next
                num += 1
        else:
            reverse_index = self.count - index - 1
            num = 0
            node = self.tail_node.prev
            while node:
                if num == reverse_index:
                    delete_node = node
                node = node.prev
                num += 1
        delete_node.prev.next = delete_node.next
        delete_node.next.prev = delete_node.prev
        delete_node.prev = None
        delete_node.next = None
        self.count -= 1

    def delete_head(self):
        if self.count > 0:
            self.deleteAtIndex(0)

    def delete_tail(self):
        if self.count > 0:
            self.deleteAtIndex(self.count - 1)

    def get_head(self):
        if self.count <= 0:
            return None
        return self.get(0)

    def get_tail(self):
        if self.count <= 0:
            return None
        return self.get(self.count - 1)

    def is_empty(self):
        return False if self.count > 0 else True

    def add_num(self, num):
        while not self.is_empty() and self.get_tail() < num:
            self.delete_tail()
        self.addAtTail(num)

    def pop_head(self):
        if not self.is_empty():
            num = self.get_head()
            self.delete_head()
            return num
        return None


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_linked_list = MyLinkedList()
        result_list = []
        for i in range(len(nums) - k + 1):
            if i == 0:
                for j in range(k):
                    my_linked_list.add_num(nums[j])
                result_list.append(my_linked_list.get_head())
                continue
            if my_linked_list.get_head() == nums[i - 1]:
                my_linked_list.pop_head()
            my_linked_list.add_num(nums[i + k - 1])
            result_list.append(my_linked_list.get_head())
        return result_list


solution = Solution()
solution.maxSlidingWindow([1], 1)