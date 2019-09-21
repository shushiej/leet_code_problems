CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;

  RETURN (
      # Write your MySQL query statement below.
        SELECT DISTINCT Salary FROM Employee Order By Salary Desc LIMIT M, 1
  );
ENDf