# LeetCode题解：0112（路径总和）

[题目链接](https://leetcode-cn.com/problems/path-sum/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 48ms (>91.80%) |
| Ans 2 (Python) | 64ms (>26.56%) |

解法一（广度优先迭代）：

```python
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
```

解法二（递归）：

```python
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
```