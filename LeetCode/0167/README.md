# LeetCode题解：0167（两数之和II - 输入有序数组）

[题目链接](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)（简单）

为第0001题的扩展，思考如何应用升序数组。

| 解法           | 执行用时        |
| :------------- | --------------- |
| Ans 1 (Python) | 40ms  (>89.25%) |
| Ans 2 (Python) | 48ms (>54.96%)  |

解法一（使用哈希表实现）：

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(numbers)):
        n = numbers[i]
        a = target - n
        if a in hashmap:
            return [hashmap[a], i + 1]
        hashmap[n] = i + 1
```

解法二（双指针解法实现）：

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    index_1 = 0
    index_2 = len(numbers) - 1
    while index_1 < index_2:
        s = numbers[index_1] + numbers[index_2]
        if s == target:
            return [index_1 + 1, index_2 + 1]
        if s < target:
            index_1 += 1
        else:
            index_2 -= 1
```