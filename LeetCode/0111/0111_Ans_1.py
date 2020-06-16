from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            if node.right is None:
                return helper(node.left) + 1
            if node.left is None:
                return helper(node.right) + 1
            return min(helper(node.left), helper(node.right)) + 1
        return helper(root)


if __name__ == "__main__":
    print(Solution().minDepth(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # 2
    print(Solution().minDepth(build_TreeNode([1, 2])))
    print(Solution().minDepth(build_TreeNode([1, 2, 3, 4, 5])))
