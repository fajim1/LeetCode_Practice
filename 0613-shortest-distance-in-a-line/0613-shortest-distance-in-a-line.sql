# Write your MySQL query statement below

SELECT min(dist) as shortest  FROM (
SELECT abs(p1.x-p2.x) as dist
FROM Point p1 JOIN Point p2
) T1
WHERE dist !=0