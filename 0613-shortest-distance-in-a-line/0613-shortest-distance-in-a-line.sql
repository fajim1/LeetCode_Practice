# Write your MySQL query statement below


SELECT min(abs(p1.x-p2.x)) as shortest 
FROM Point p1 JOIN Point p2
WHERE abs(p1.x-p2.x)!=0