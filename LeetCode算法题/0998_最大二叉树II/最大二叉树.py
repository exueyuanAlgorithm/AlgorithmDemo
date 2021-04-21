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
        self.parent = None


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        root = self.recreate(root)
        if not root:
            return TreeNode(val)
        search_node = root
        while search_node.right:
            search_node.right.parent = search_node
            search_node = search_node.right
        add_tree_node = TreeNode(val)
        search_node.right = add_tree_node
        add_tree_node.parent = search_node

        while add_tree_node.parent and add_tree_node.parent.val < add_tree_node.val:
            temp_parent = add_tree_node.parent
            temp_parent_parent = temp_parent.parent
            if temp_parent_parent:
                temp_parent_parent.right = add_tree_node
            add_tree_node.parent = temp_parent_parent
            add_tree_node_left_temp = add_tree_node.left
            temp_parent.parent = add_tree_node
            add_tree_node.left = temp_parent
            temp_parent.right = add_tree_node_left_temp
            if add_tree_node_left_temp:
                add_tree_node_left_temp.parent = temp_parent
        if add_tree_node.parent:
            return root
        else:
            return add_tree_node

    def recreate(self, root):
        if not root:
            return None
        new_root = TreeNode(root.val)
        left_chid = self.recreate(root.left)
        right_chid = self.recreate(root.right)
        new_root.left = left_chid
        new_root.right = right_chid
        if left_chid:
            left_chid.parent = new_root
        if right_chid:
            right_chid.parent = new_root
        return new_root


tree_list = [4, 1, 3, None, None, 2]
root = list_to_tree_node(tree_list)
solution = Solution()
new_root = solution.insertIntoMaxTree(root, 5)
solution_list = tree_node_to_list(new_root)
print(solution_list)
