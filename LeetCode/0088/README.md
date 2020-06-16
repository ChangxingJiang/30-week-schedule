# LeetCode题解：0088（合并两个有序数组）

[题目链接](https://leetcode-cn.com/problems/merge-sorted-array/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 36ms (>87.78%) |

解法一（双指针从后向前遍历填写）：

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    index_1 = m - 1
    index_2 = n - 1
    for i in range(m + n - 1, -1, -1):
        if index_1 < 0 or (index_2 >= 0 and nums2[index_2] > nums1[index_1]):
            nums1[i] = nums2[index_2]
            index_2 -= 1
        else:
            nums1[i] = nums1[index_1]
            index_1 -= 1
```