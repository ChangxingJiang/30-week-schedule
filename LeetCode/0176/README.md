# LeetCode题解：0176（第二高的薪水）

[题目链接](https://leetcode-cn.com/problems/second-highest-salary/)（简单）

| 解法        | 执行用时        |
| :---------- | --------------- |
| Ans 1 (SQL) | 157ms (>54.65%) |

解法一：

```sql
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) from Employee);
```