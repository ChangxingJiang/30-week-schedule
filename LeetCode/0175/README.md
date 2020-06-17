# LeetCode题解：0175（合并两个表）

[题目链接](https://leetcode-cn.com/problems/combine-two-tables/)（简单）

| 解法        | 执行用时        |
| :---------- | --------------- |
| Ans 1 (SQL) | 285ms (>29.61%) |
| Ans 2 (SQL) | 277ms (>34.01%) |

解法一：

```sql
SELECT person.FirstName, person.LastName, address.City, address.State
FROM person
         LEFT JOIN Address ON (person.PersonId = address.PersonId);
```

解法二（简洁化的解法一）：

```sql
SELECT FirstName, LastName, City, State
FROM person
         LEFT JOIN Address USING (PersonId);
```