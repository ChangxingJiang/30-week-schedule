from LeetCode.toolkit import TreeNode, build_TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if (p is not None and q is not None) != (p is not None or q is not None):
            return False

        node_list = [(p, q)]
        while len(node_list) > 0:
            pp, qq = node_list[0]
            if pp.val != qq.val:
                return False
            if (pp.left is not None and qq.left is not None) != (pp.left is not None or qq.left is not None):
                return False
            if (pp.right is not None and qq.right is not None) != (pp.right is not None or qq.right is not None):
                return False
            if pp.left:
                node_list.append((pp.left, qq.left))
            if pp.right:
                node_list.append((pp.right, qq.right))
            node_list.pop(0)
        return True


if __name__ == "__main__":
    print(Solution().isSameTree(build_TreeNode([1, 2, 3]), build_TreeNode([1, 2, 3])))  # True
    print(Solution().isSameTree(build_TreeNode([1, 2]), build_TreeNode([1, None, 2])))  # False
    print(Solution().isSameTree(build_TreeNode([1, 2, 1]), build_TreeNode([1, 1, 2])))  # False
