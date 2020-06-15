# LeetCode题解：0026（删除排序数组中的重复值）

[题目链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)（简单）

| 解法           | 执行用时        |
| -------------- | --------------- |
| Ans 1 (Python) | 60ms (>45.26%)  |
| Ans 2 (Python) | 1040ms (>8.16%) |
| Ans 3 (Python) | 52ms (>62.63%)  |

解法一（遍历寻找重复值,，再遍历移除）：

```python
def removeDuplicates(self, nums: List[int]) -> int:
    hashset = set()
    del_list = []
    for i in range(len(nums)):
        d = nums[i]
        if d not in hashset:
            hashset.add(d)
        else:
            del_list.append(i)

    for i in del_list[::-1]:
        nums.pop(i)

    return len(nums)
```

解法二（一次遍历直接移除）：

```python
def removeDuplicates(self, nums: List[int]) -> int:
    for i in range(len(nums))[::-1]:
        d = nums[i]
        if d in nums[i + 1:]:
            nums.pop(i)
    return len(nums)
```

解法三（注意到排序数组的条件）：

```python
def removeDuplicates(self, nums: List[int]) -> int:
    m = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i]:
            m += 1
            nums[m] = nums[i + 1]
    return m + 1
```