# LeetCode题解：0027（移除元素）

[题目链接](https://leetcode-cn.com/problems/remove-element/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 40ms (>67.81%) |
| Ans 2 (Python) | 52ms (>14.22%) |

解法一（遍历数组移除元素）：

```python
def removeElement(self, nums: List[int], val: int) -> int:
    m = 0
    for i in range(len(nums)):
        d = nums[i]
        if d != val:
            nums[m] = nums[i]
            m += 1
    return m
```

解法二（循环使用remove移除所有该元素）：

```python
def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)
```