# LeetCode题解：0070（爬楼梯）

[题目链接](https://leetcode-cn.com/problems/climbing-stairs/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 40ms (>63.45%) |
| Ans 2 (Python) | 36ms (>83.39%) |
| Ans 3 (Python) | 28ms (>98.73%) |

解法一（遍历滚动数组）：

```python
def climbStairs(self, n: int) -> int:
        def climbStairs(self, n: int) -> int:
        a = 0
        b = 0
        c = 1
        for i in range(n):
            a = b
            b = c
            c = a + b
        return c
```

解法二（使用哈希表存储计算结果）：

```python
def climbStairs(self, n: int) -> int:
    hashmap = {1: 1, 2: 2}
    if n < 3:
        return hashmap[n]
    for i in range(3, n + 1):
        hashmap[i] = hashmap[i - 1] + hashmap[i - 2]
    return hashmap[n]
```

解法三（通项公式）：

由特征方程解出，菲波那切数列的通项公式为：
$$
f(n)=\frac{1}{\sqrt{5}}[(\frac{1+\sqrt{5}}{2})^n-(\frac{1-\sqrt{5}}{2})^n]
$$

```python
def climbStairs(self, n: int) -> int:
    sqrt5 = math.sqrt(5)
    return int((pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)) / sqrt5)
```