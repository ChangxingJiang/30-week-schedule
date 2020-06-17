SELECT person.FirstName, person.LastName, address.City, address.State
FROM person
         LEFT JOIN Address ON (person.PersonId = address.PersonId);
