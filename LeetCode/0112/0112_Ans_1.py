from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        node_dict = {root: root.val}
        while len(node_dict) > 0:
            temp_node_dict = {}
            for node in node_dict:
                node_value = node_dict[node]
                if node.left is None and node.right is None:
                    if node_value == sum:
                        return True
                if node.left is not None:
                    temp_node_dict[node.left] = node_value + node.left.val
                if node.right is not None:
                    temp_node_dict[node.right] = node_value + node.right.val
            node_dict = temp_node_dict
        return False


if __name__ == "__main__":
    print(Solution().hasPathSum(build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22))
    print(Solution().hasPathSum(build_TreeNode([1]), 1))
