# Write your MySQL query statement below
WITH starts as (
    SELECT * 
    FROM Activity
    WHERE activity_type  = "start"
    ORDER BY machine_id asc, process_id asc
                ),
                
ends as (
    SELECT * 
    FROM Activity
    WHERE activity_type  = "end"
    ORDER BY machine_id asc, process_id asc
                )
                
SELECT starts.machine_id, ROUND(AVG(ends.timestamp-starts.timestamp),3) as processing_time 
FROM starts INNER JOIN ends 
ON starts.machine_id = ends.machine_id 
AND starts.process_id  = ends.process_id  
GROUP BY starts.machine_id