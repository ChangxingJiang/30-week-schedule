from LeetCode.toolkit import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if (p is not None and q is not None) != (p is not None or q is not None):
            return False

        node_list = [(p, q)]
        while node_list is not None:
            pp, qq = node_list[0]
            if pp.val != qq.val:
                return False
            if (pp.left is not None and qq.left is not None) != (pp.left is not None or qq.left is not None):
                return False
            if (pp.right is not None and qq.right is not None) != (pp.right is not None or qq.right is not None):
                return False
            if pp.left:
                node_list.append((pp.left, qq.left))
            if pp.right:
                node_list.append((pp.right, qq.right))
            node_list.pop(0)
        return True


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    tree_2 = TreeNode(1)
    tree_2.left = TreeNode(2)
    tree_2.right = TreeNode(3)
    print(Solution().isSameTree(tree_1, tree_2))  # True

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_2 = TreeNode(1)
    tree_2.right = TreeNode(2)
    print(Solution().isSameTree(tree_1, tree_2))  # False

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(1)
    tree_2 = TreeNode(1)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(2)
    print(Solution().isSameTree(tree_1, tree_2))  # False
