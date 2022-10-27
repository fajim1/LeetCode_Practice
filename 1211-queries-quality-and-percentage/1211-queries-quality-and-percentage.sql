# Write your MySQL query statement below
SELECT query_name,round(AVG(rating/position),2) as quality, round(AVG(rating < 3)*100,2) as poor_query_percentage 
FROM Queries
GROUP BY query_name