# LeetCode题解：0181（超过经理收入的员工）

[题目链接](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/)（简单）

| 解法        | 执行用时        |
| :---------- | --------------- |
| Ans 1 (SQL) | 347ms (>38.13%) |

解法一：

```sql
SELECT a.Name as Employee
FROM employee as a,
     employee as b
WHERE a.Salary > b.Salary
  AND a.ManagerId = b.Id;
```