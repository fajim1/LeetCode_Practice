# Write your MySQL query statement below

WITH immediate as (
    SELECT customer_id 
    FROM Delivery
    GROUP BY customer_id
    Having min(order_date) = min(customer_pref_delivery_date) 
    )
    
SELECT ROUND((SELECT COUNT(*) FROM immediate)*100/COUNT(Distinct(customer_id )),2) as immediate_percentage 
FROM Delivery
