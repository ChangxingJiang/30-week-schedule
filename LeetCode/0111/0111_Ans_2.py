from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 1
        node_list = [root]
        while len(node_list) > 0:
            temp_node_list = []
            for node in node_list:
                if node.left is None and node.right is None:
                    return level
                if node.left is not None:
                    temp_node_list.append(node.left)
                if node.right is not None:
                    temp_node_list.append(node.right)
            node_list = temp_node_list
            level += 1
        return level


if __name__ == "__main__":
    print(Solution().minDepth(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # 2
    print(Solution().minDepth(build_TreeNode([1, 2])))
    print(Solution().minDepth(build_TreeNode([1, 2, 3, 4, 5])))
