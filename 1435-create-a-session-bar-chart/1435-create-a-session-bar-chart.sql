# Write your MySQL query statement below


WITH cte_1 as (SELECT *,CASE
    WHEN duration/60 >= 0 and duration/60 <5 THEN "[0-5>"
    WHEN duration/60 >= 5 and duration/60 <10 THEN "[5-10>"
    WHEN duration/60 >= 10 and duration/60 <15 THEN "[10-15>"
    ELSE "15 or more"
    END as bin
    FROM Sessions
    ),
    
cte_2 AS(
SELECT '[0-5>' as bin
union
SELECT '[5-10>' as bin
union
SELECT '[10-15>' as bin 
union
SELECT '15 or more' as bin)



    
SELECT cte_2.bin, COALESCE(COUNT(cte_1.session_id),0) as total 
FROM cte_2
LEFT JOIN cte_1
ON cte_2.bin = cte_1.bin
GROUP BY cte_2.bin