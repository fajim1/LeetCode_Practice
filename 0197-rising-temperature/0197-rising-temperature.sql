# Write your MySQL query statement below
SELECT W1.id
FROM Weather W1 
INNER JOIN Weather W2 
ON DATEDIFF(W1.recordDate, W2.recordDate) = 1
AND W1.Temperature > W2.Temperature
