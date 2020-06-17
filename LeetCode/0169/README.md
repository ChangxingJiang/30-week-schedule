# LeetCode题解：0169（多数元素）

[题目链接](https://leetcode-cn.com/problems/majority-element/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 52ms (>65.53%) |
| Ans 2 (Python) | 40ms (>95.36%) |
| Ans 3 (Python) | 56ms (>52.76%) |

解法一（使用哈希表）：

```python
def majorityElement(self, nums: List[int]) -> int:
    s = len(nums) / 2
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    for num, count in hashmap.items():
        if count > s:
            return num
```

解法二（排序法；这就很Python）：

```python
def majorityElement(self, nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]
```

解法三（摩尔投票法）：

```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        if candidate == n:
            count += 1
        else:
            count -= 1
    return candidate
```