#210ms 

Select DISTINCT a.Email from Person AS a JOIN Person AS b WHERE a.Email = b.Email AND a.ID != b.Id