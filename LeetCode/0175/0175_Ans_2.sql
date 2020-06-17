SELECT FirstName, LastName, City, State
FROM person
         LEFT JOIN Address USING (PersonId);
