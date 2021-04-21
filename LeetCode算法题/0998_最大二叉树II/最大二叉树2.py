def list_to_tree_node(tree_list):
    if not tree_list:
        return None
    tree_node_list = []
    i = 0
    root = None
    for item in tree_list:
        tree_node = None
        if isinstance(item, int):
            tree_node = TreeNode(item)
        if not tree_node_list:
            root = tree_node
            tree_node_list.append((tree_node, 0))
            tree_node_list.append((tree_node, 1))
            continue
        else:
            xulie_tree_node = tree_node_list[i]
            if xulie_tree_node[1] == 0:
                xulie_tree_node[0].left = tree_node
                i += 1
            if xulie_tree_node[1] == 1:
                xulie_tree_node[0].right = tree_node
                i += 1
            if tree_node:
                tree_node_list.append((tree_node, 0))
                tree_node_list.append((tree_node, 1))
    return root


def tree_node_to_list(root):
    result_list = []
    if not root:
        return result_list
    node_list = [root]
    i = 0
    while i < len(node_list):
        node = node_list[i]
        i += 1
        if node:
            result_list.append(node.val)
            node_list.append(node.left)
            node_list.append(node.right)
        else:
            result_list.append(None)

    for j in range(len(result_list) - 1, -1, -1):
        num = result_list[j]
        if not num:
            result_list.pop(j)
        else:
            break
    return result_list


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val < val:
            tmp = TreeNode(val)
            tmp.left = root
            return tmp
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


tree_list = [4, 1, 3, None, None, 2]
root = list_to_tree_node(tree_list)
solution = Solution()
new_root = solution.insertIntoMaxTree(root, 5)
solution_list = tree_node_to_list(new_root)
print(solution_list)
