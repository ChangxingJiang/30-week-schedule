SELECT a.Name as Employee
FROM employee as a,
     employee as b
WHERE a.Salary > b.Salary
  AND a.ManagerId = b.Id;