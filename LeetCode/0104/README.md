# LeetCode题解：0104（二叉树的最大深度）

[题目链接](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 44ms (>96.19%) |

解法一（递归计算深度）：

```python
def maxDepth(self, root: TreeNode) -> int:
    def get_depth(node):
        if node is None:
            return 0
        return max(get_depth(node.left), get_depth(node.right)) + 1
    return get_depth(root)
```

