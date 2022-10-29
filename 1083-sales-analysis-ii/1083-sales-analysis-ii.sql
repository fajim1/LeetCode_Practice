# Write your MySQL query statement below
SELECT s.buyer_id
FROM Sales s JOIN Product p USING(product_id)
GROUP BY s.buyer_id
HAVING SUM(p.product_name = 'S8') > 0 AND SUM(p.product_name = 'iPhone') = 0