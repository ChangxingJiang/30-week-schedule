# LeetCode题解：0111（二叉树的最小深度）

[题目链接](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 52ms (>85.44%) |
| Ans 2 (Python) | 48ms (>94.35%) |

解法一（深度优先递归）：

```python
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
```

解法二（广度优先迭代）：

```python
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
```

