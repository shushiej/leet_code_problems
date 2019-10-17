#246 ms

SELECT PERSON.FirstName, Person.LastName, Address.City, Address.State FROM PERSON LEFT JOIN ADDRESS 
    ON Person.PersonId = Address.PersonId
UNION 
SELECT PERSON.FirstName, Person.LastName, Address.City, Address.State FROM PERSON RIGHT JOIN ADDRESS 
    ON Person.PersonId = Address.PersonId
    WHERE Person.PersonId = Address.PersonId