SELECT b.Id FROM Weather a 
    INNER JOIN 
    Weather b
WHERE DATEDIFF(b.RecordDate, a.RecordDate) = 1 AND b.Temperature > a.Temperature