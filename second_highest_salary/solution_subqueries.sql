#142ms

SELECT MAX(Salary) as SecondHighestSalary From Employee WHERE Salary < ( SELECT Max(Salary) FROM Employee)