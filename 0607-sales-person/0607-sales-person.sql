# Write your MySQL query statement below

SELECT name 
FROM SalesPerson
WHERE sales_id not in (

SELECT SalesPerson.sales_id
FROM SalesPerson
LEFT JOIN Orders
ON Orders.sales_id = SalesPerson.sales_id
LEFT JOIN Company
ON Orders.com_id = Company.com_id
WHERE Company.name = "RED"
)