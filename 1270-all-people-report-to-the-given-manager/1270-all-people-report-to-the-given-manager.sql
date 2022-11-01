# Write your MySQL query statement below

SELECT employee_id
FROM Employees
WHERE manager_id in
    (
    SELECT employee_id
    FROM Employees

    WHERE manager_id in (
        SELECT employee_id  
        FROM Employees 
        WHERE manager_id = 1
        )
    )
AND employee_id!=1