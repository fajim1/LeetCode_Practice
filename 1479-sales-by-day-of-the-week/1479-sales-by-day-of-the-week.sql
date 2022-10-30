# Write your MySQL query statement below
SELECT item_category as Category    ,
SUM(CASE WHEN DAYNAME(order_date) = "Monday" THEN quantity ELSE 0 END) AS Monday,
SUM(CASE WHEN DAYNAME(order_date) = "Tuesday" THEN quantity ELSE 0 END) AS Tuesday,
SUM(CASE WHEN DAYNAME(order_date) = "Wednesday" THEN quantity ELSE 0 END) AS Wednesday,
SUM(CASE WHEN DAYNAME(order_date) = "Thursday" THEN quantity ELSE 0 END) AS Thursday,
SUM(CASE WHEN DAYNAME(order_date) = "Friday" THEN quantity ELSE 0 END) AS Friday,
SUM(CASE WHEN DAYNAME(order_date) = "Saturday" THEN quantity ELSE 0 END) AS Saturday,
SUM(CASE WHEN DAYNAME(order_date) = "Sunday" THEN quantity ELSE 0 END) AS Sunday
FROM Items LEFT JOIN Orders USING(item_id)
GROUP BY Category   
ORDER BY Category   