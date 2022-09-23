# Write your MySQL query statement below

SELECT email
FROM Person
Group by email 
Having count(email) >1