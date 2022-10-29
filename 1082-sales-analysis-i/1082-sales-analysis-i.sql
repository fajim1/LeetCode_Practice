# Write your MySQL query statement below

WITH t1 as (SELECT seller_id, sum(price) as total
FROM Sales
GROUP BY seller_id
            )

SELECT seller_id
FROM t1
WHERE total = (
    SELECT max(total)
    FROM t1
    )