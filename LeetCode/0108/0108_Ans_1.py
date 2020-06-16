from typing import List

from LeetCode.toolkit import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def get_node(a, b):
            if a > b:
                return None
            t = (a + b) // 2
            node = TreeNode(nums[t])
            node.left = get_node(a, t - 1)
            node.right = get_node(t + 1, b)
            return node

        return get_node(0, len(nums) - 1)


if __name__ == "__main__":
    print(Solution().sortedArrayToBST([-10, -3,  0, 5, 9]))
