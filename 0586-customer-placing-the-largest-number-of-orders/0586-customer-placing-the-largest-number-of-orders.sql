# Write your MySQL query statement below

SELECT customer_number FROM (
SELECT customer_number,COUNT(*) as total_orders
FROM Orders
GROUP BY customer_number
ORDER BY total_orders desc limit 1
    ) as A