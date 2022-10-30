# Write your MySQL query statement below
SELECT employee_id, 
CASE 
    WHEN name not like "M%" and (employee_id%2) = 1 THEN salary
    ELSE 0
END as bonus
FROM Employees
ORDER BY employee_id asc