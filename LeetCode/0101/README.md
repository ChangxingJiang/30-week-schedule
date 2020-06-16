# LeetCode题解：0101（对称二叉树）

[题目链接](https://leetcode-cn.com/problems/symmetric-tree/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 36ms (>96.13%) |

解法一（递归比较）：

```python
def isSymmetric(self, root: TreeNode) -> bool:
    def is_symmetric(p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

    if root is None:
        return True
    return is_symmetric(root.left, root.right)
```

与题目100非常相似，是题目100的延伸。