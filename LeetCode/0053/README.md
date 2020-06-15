# LeetCode题解：0053（最大子序和）

[题目链接](https://leetcode-cn.com/problems/maximum-subarray/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 36ms (>98.88%) |

解法一（使用now存储当前状态maximum存储最大值，遍历实现）：

```python
def maxSubArray(self, nums: List[int]) -> int:
    maximum = nums[0]
    now = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        if maximum < 0 and n > maximum:
            maximum = n
            now = n
        else:
            now += n
            if now < n:
                now = n
            if now > maximum:
                maximum = now
    return maximum
```