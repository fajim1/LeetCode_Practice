# Write your MySQL query statement below

SELECT 
product_id,
SUM(CASE WHEN store = 'store1' THEN price ELSE null END) as store1,
SUM(CASE WHEN store = 'store2' THEN price ELSE null END) as store2,
SUM(CASE WHEN store = 'store3' THEN price ELSE null END) as store3
FROM Products
GROUP BY product_id