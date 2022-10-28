# Write your MySQL query statement below

SELECT name 
FROM SalesPerson
WHERE sales_id not in (

SELECT Orders.sales_id
FROM Orders 
INNER JOIN Company 
ON Orders.com_id = Company.com_id
WHERE Company.name = "RED"
)