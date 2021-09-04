# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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





root = list_to_tree_node([2, None, 3, 5, 3, 8, 7, None, 6])
result_list = tree_node_to_list(root)
print(result_list)

# print(list_to_tree_node([2, None, 3, 5, 3, 8, 7, None, 6]))
