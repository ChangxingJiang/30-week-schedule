from typing import List

from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        node_list = [root]
        while len(node_list) > 0:
            level_val = []
            temp_node_list = []
            for node in node_list:
                level_val.append(node.val)
                if node.left:
                    temp_node_list.append(node.left)
                if node.right:
                    temp_node_list.append(node.right)
            ans.append(level_val)
            node_list = temp_node_list
        ans.reverse()
        return ans


if __name__ == "__main__":
    print(Solution().levelOrderBottom(build_TreeNode([3, 9, 20, None, None, 15, 7])))
