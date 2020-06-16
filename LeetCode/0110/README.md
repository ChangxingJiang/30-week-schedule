# LeetCode题解：0110（平衡二叉树）

[题目链接](https://leetcode-cn.com/problems/balanced-binary-tree/)（简单）

高度平衡二叉树是指每个节点左右两个子树的高度差的绝对值不超过1个。

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 60ms (>84.26%) |

解法一（遍历计算是否平衡）：

```python
def isBalanced(self, root: TreeNode) -> bool:
    def helper(node):
        if node is None:
            return 0, True
        left_depth, left_is_balance = helper(node.left)
        right_depth, right_is_balance = helper(node.right)
        is_balance = abs(left_depth - right_depth) <= 1
        # print(node.val, max(left_depth, right_depth) + 1, abs(left_depth - right_depth) > 1)
        return max(left_depth, right_depth) + 1, is_balance and left_is_balance and right_is_balance

    return helper(root)[1]
```