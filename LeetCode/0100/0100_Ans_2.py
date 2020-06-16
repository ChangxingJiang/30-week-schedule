from LeetCode.toolkit import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
