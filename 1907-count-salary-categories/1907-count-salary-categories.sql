# Write your MySQL query statement below
WITH CATS as ( 
    
SELECT account_id,
CASE 
    WHEN income < 20000 THEN "Low Salary"
    WHEN income > 50000  Then "High Salary"
    ELSE "Average Salary"
END as category
FROM Accounts
),

ALL_CATS AS(        
SELECT "Low Salary" AS Category
UNION 
SELECT "Average Salary" AS Category
UNION 
SELECT "High Salary" AS Category
)

SELECT ALL_CATS.category,count(account_id) as accounts_count 
FROM ALL_CATS
LEFT JOIN CATS
ON ALL_CATS.Category = CATS.Category
GROUP BY CATS.category