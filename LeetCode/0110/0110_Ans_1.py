from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node is None:
                return 0, True
            left_depth, left_is_balance = helper(node.left)
            right_depth, right_is_balance = helper(node.right)
            is_balance = abs(left_depth - right_depth) <= 1
            # print(node.val, max(left_depth, right_depth) + 1, abs(left_depth - right_depth) > 1)
            return max(left_depth, right_depth) + 1, is_balance and left_is_balance and right_is_balance

        return helper(root)[1]


if __name__ == "__main__":
    print(Solution().isBalanced(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # True
    print(Solution().isBalanced(build_TreeNode([1, 2, 2, 3, 3, None, None, 4, 4])))  # False
