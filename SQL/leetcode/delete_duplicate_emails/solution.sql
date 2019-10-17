DELETE a FROM Person a
    INNER JOIN
    Person b
WHERE
    a.Id > b.Id AND a.Email = b.Email