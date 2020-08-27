# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def setTreeNode(treeNodeList):
    root = None
    needAddNodeList = []
    if treeNodeList:
        root = TreeNode
        root.val = treeNodeList[0]
        needAddNodeList.append((root, 0))
        needAddNodeList.append((root, 1))
    else:
        return root
    i = 0
    for nodeData in treeNodeList[1:]:
        treeNode = TreeNode
        treeNode.val = nodeData
        getRoot = needAddNodeList[i][0]
        leftRight = needAddNodeList[i][1]
        if leftRight == 0:
            getRoot.left = treeNode
        else:
            getRoot.right = treeNode
        needAddNodeList.append((treeNode, 0))
        needAddNodeList.append((treeNode, 1))
        i += 1
    return root


def forEachTreeNodeList(root):
    pass

print(setTreeNode([2, 3, 5, 3, 8, 7]))
