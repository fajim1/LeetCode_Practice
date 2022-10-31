# Write your MySQL query statement below
WITH temp1 as (
    SELECT customer_id,product_id,count(*) as count
    FROM Orders
    GROUP BY customer_id,product_id
    ORDER BY customer_id asc,product_id asc
    )

SELECT customer_id,temp2.product_id,Products.product_name FROM(
    SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY count DESC) as Rank1 
    FROM temp1
    ) as temp2
INNER JOIN Products
ON temp2.product_id = Products.product_id 
WHERE Rank1 = 1