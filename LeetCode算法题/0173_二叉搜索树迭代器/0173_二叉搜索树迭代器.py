
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def bianli_root(self, root:TreeNode, num_list):
        if not root:
            return
        self.bianli_root(root.left, num_list)
        num_list.append(root.val)
        self.bianli_root(root.right, num_list)


    def __init__(self, root: TreeNode):
        self.num_list = []
        self.bianli_root(root, self.num_list)
        self.position = -1
        pass


    def next(self) -> int:
        self.position += 1
        return self.num_list[self.position]


    def hasNext(self) -> bool:
        if self.position + 1 < len(self.num_list):
            return True
        else:
            return False