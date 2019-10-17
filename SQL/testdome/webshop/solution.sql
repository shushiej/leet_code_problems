SELECT i.name as Item,  
       s.name as Seller 
  FROM sellers as s
  JOIN items as i 
  ON s.id = i.sellerId
  WHERE s.rating > 4