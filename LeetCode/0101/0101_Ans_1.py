from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_symmetric(p: TreeNode, q: TreeNode):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

        if root is None:
            return True
        return is_symmetric(root.left, root.right)


if __name__ == "__main__":
    print(Solution().isSymmetric(build_TreeNode([1, 2, 2, 3, 4, 4, 3])))  # True
    print(Solution().isSymmetric(build_TreeNode([1, 2, 2, None, 3, None, 3])))  # False
