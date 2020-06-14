# LeetCode题解：0001（两数之和）

[题目链接](https://leetcode-cn.com/problems/two-sum/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时         | 内存消耗         |
| -------------- | ---------- | ---------- | ---------------- | ---------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 5564ms (>21.06%) | 14.5MB (>13.41%) |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     | 872ms (>41.68%)  | 14.5MB (>13.41%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 56ms (>77.63%)   | 15.1MB (>5.48%)  |

解法一（直接两次遍历）：

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

解法二（使用使用列表的\_\_contain()\_\_方法替换第二层遍历）：

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        another = target - nums[i]
        if another in nums[(i + 1):]:
            return [i, nums[(i + 1):].index(another) + i + 1]
```

> 其中列表的contain or in方法的时间复杂度为$O(N)$，index方法的时间复杂度为$O(N)$（[参考文献](https://www.jianshu.com/p/a2c98df9cfae)）

解法三（使用哈希表存储已经遍历过的数，因为查找哈希表的时间复杂度为$O(1)$）：

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
```