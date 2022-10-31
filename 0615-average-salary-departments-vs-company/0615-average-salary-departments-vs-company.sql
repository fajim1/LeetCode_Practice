# Write your MySQL query statement below
WITH temp1 as (
    SELECT AVG(amount) as avg_amount_per_month, LEFT(Salary.pay_date,7) as pay_month
    FROM Salary
    GROUP BY pay_month
    ORDER BY pay_month asc 
),

temp2 as (
    SELECT department_id,LEFT(Salary.pay_date,7) as pay_month,AVG(amount) as avg_amount_per_month_per_dept
    FROM Salary
    INNER JOIN Employee
    ON Salary.employee_id = Employee.employee_id
    GROUP BY department_id,pay_month
    ORDER BY pay_month asc
    )

SELECT temp1.pay_month ,department_id,
CASE
    WHEN avg_amount_per_month_per_dept > avg_amount_per_month THEN "higher"
    WHEN avg_amount_per_month_per_dept < avg_amount_per_month THEN "lower"
    ELSE "same"
    END as comparison
FROM temp1
INNER JOIN temp2
ON temp1.pay_month = temp2.pay_month
ORDER BY department_id asc,temp1.pay_month asc