# LeetCode题解：0035（搜索插入位置）

[题目链接](https://leetcode-cn.com/problems/search-insert-position/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 32ms (>96.96%) |

解法一（遍历寻找插入位置）：

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    len_num = len(nums)
    for i in range(len_num):
        if nums[i] >= target:
            return i
    return len_num
```



