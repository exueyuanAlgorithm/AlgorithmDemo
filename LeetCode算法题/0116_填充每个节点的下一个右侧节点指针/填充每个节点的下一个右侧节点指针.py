# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        if not root.left:
            return root
        root.left.next = root.right
        self.connect_left_right(root.left, root.right)
        return root

    def connect_left_right(self, left, right):
        if not left:
            return
        if not left.left:
            return
        left.left.next = left.right
        right.left.next = right.right
        left.right.next = right.left
        self.connect_left_right(left.left, left.right)
        self.connect_left_right(right.left, right.right)
        self.connect_left_right(left.right, right.left)
