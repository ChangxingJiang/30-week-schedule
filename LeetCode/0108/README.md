# LeetCode题解：0108（将有序数组转换为二叉搜索树）

[题目链接](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)（简单）

高度平衡二叉树是指每个节点左右两个子树的高度差的绝对值不超过1个。

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 56ms (>79.75%) |

解法一（中序遍历）：

```python
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def helper(left, right):
        if left > right:
            return None

        p = (left + right) // 2

        root = TreeNode(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root

    return helper(0, len(nums) - 1)
```