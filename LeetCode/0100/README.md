# LeetCode题解：0100（相同的树）

[题目链接](https://leetcode-cn.com/problems/same-tree/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 40ms (>68.56%) |
| Ans 2 (Python) | 40ms (>68.56%) |

解法一（暴力解树）：

```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if (p is not None and q is not None) != (p is not None or q is not None):
        return False

    node_list = [(p, q)]
    while node_list is not None:
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
```

解法二（递归解树）：

```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```