# Write your MySQL query statement below

SELECT name as Customers
FROM Customers
left join Orders
ON Customers.id = Orders.customerID
WHERE customerID is null