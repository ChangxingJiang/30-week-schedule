from LeetCode.toolkit import TreeNode, build_TreeNode


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
    print(Solution().isSameTree(build_TreeNode([1, 2, 3]), build_TreeNode([1, 2, 3])))  # True
    print(Solution().isSameTree(build_TreeNode([1, 2]), build_TreeNode([1, None, 2])))  # False
    print(Solution().isSameTree(build_TreeNode([1, 2, 1]), build_TreeNode([1, 1, 2])))  # False
