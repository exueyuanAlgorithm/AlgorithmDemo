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

        current = root
        child_current_root = None
        child_current = None
        while current:
            if current.left:
                if not child_current_root:
                    child_current_root = current.left
                    child_current = child_current_root
                else:
                    child_current.next = current.left
                    child_current = child_current.next
            if current.right:
                if not child_current_root:
                    child_current_root = current.right
                    child_current = child_current_root
                else:
                    child_current.next = current.right
                    child_current = child_current.next
            current = current.next
        self.connect(child_current_root)
        return root

