class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isHaveCircle(linkNode: ListNode):
    linkNode1 = linkNode
    linkNode2 = linkNode
    while True:
        if linkNode1.next is not None:
            linkNode1 = linkNode1.next
        else:
            return False
        if linkNode2.next is not None and linkNode2.next.next is not None:
            linkNode2 = linkNode2.next.next
        else:
            return False
        if linkNode1 == linkNode2:
            return True


