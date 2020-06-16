from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        def helper(node, value):
            if node.left is None and node.right is None:
                return value == sum
            if node.left is None:
                return helper(node.right, value + node.right.val)
            if node.right is None:
                return helper(node.left, value + node.left.val)
            return helper(node.right, value + node.right.val) or helper(node.left, value + node.left.val)

        return helper(root, root.val)


if __name__ == "__main__":
    print(Solution().hasPathSum(build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22))  # True
    print(Solution().hasPathSum(build_TreeNode([1]), 1))  # True
