# Write your MySQL query statement below

WITH immediate as (
    SELECT *
    FROM Delivery
    WHERE order_date = customer_pref_delivery_date 
    )
    
SELECT ROUND((SELECT COUNT(*) FROM immediate)*100/COUNT(*),2) as immediate_percentage 
FROM Delivery