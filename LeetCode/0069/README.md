# LeetCode题解：0069（x的平方根）

[题目链接](https://leetcode-cn.com/problems/sqrtx/)（简单）

| 解法           | 执行用时         |
| :------------- | ---------------- |
| Ans 1 (Python) | 44ms (>83.07%)   |
| Ans 2 (Python) | 1920ms (>10.71%) |
| Ans 3 (Python) | 60ms (>31.49%)   |
| Ans 4 (Python) | 48ms (>58.91%)   |
| Ans 5 (Python) | 40ms (>93.03%)   |

解法一（直接使用Python原生函数计算）：

```python
def mySqrt(self, x: int) -> int:
    return int(pow(x, 0.5))
```

解法二（因只需要取整，得到如下遍历法）：

```python
def mySqrt(self, x: int) -> int:
    num = 0
    for i in range(1, x + 1):
        if i * i > x:
            return num
        num = i
    return num
```

解法三（二分查找）：

```python
def mySqrt(self, x: int) -> int:
    def find(a, b):
        if b - a <= 1:
            # print("R:", a, b)
            return a
        c = int((a + b) / 2)
        # print("C:", a, b, c, c * c > x)
        if c * c > x:
            return find(a, c)
        else:
            return find(c, b)
    return find(0, x + 1)
```

解法四（牛顿迭代法）：

```python
def mySqrt(self, x: int) -> int:
    num = x
    while int(num * num) > x:
        num = (num + x / num) / 2
    return int(num)
```

解法五（牛顿迭代法整除）：

```python
def mySqrt(self, x: int) -> int:
    num = x
    while num * num > x:
        num = (num + x / num) // 2
    return int(num)
```

参考文献（题解）：https://leetcode-cn.com/problems/sqrtx/solution/jing-dian-ti-mu-yi-ti-duo-jie-si-chong-fang-fa-jie/

参考文献（牛顿迭代法）：https://blog.csdn.net/ccnt_2012/article/details/81837154