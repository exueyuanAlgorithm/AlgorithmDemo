from TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False

        if root.left is None:
            return self.hasPathSum(root.right, sum-root.val)
        if root.right is None:
            return self.hasPathSum(root.left, sum-root.val)

        hasPathSumLeft = self.hasPathSum(root.left, sum-root.val)
        if hasPathSumLeft:
            return True
        else:
            return self.hasPathSum(root.right, sum-root.val)

def getTreeNodeRoot():
    treeNode0 = TreeNode(5)
    treeNode1 = TreeNode(4)
    treeNode2 = TreeNode(11)
    treeNode3 = TreeNode(7)
    treeNode4 = TreeNode(2)
    treeNode5 = TreeNode(8)
    treeNode6 = TreeNode(13)
    treeNode7 = TreeNode(4)
    treeNode8 = TreeNode(1)

    treeNode0.left = treeNode1
    treeNode0.right = treeNode5
    treeNode1.left = treeNode2
    treeNode2.left = treeNode3
    treeNode2.right = treeNode4
    treeNode5.left = treeNode6
    treeNode5.right = treeNode7
    treeNode7.right = treeNode8
    return treeNode0



solution = Solution()
print(solution.hasPathSum(getTreeNodeRoot(), 22))