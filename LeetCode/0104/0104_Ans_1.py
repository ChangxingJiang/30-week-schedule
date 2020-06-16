from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(node):
            if node is None:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        return get_depth(root)


if __name__ == "__main__":
    print(Solution().maxDepth(build_TreeNode([3, 9, 20, None, None, 15, 7])))
