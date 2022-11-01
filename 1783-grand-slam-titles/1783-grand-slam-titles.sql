# Write your MySQL query statement below
WITH CTE AS 
   (
    SELECT Wimbledon AS id FROM Championships
    UNION ALL 
    SELECT Fr_open AS id FROM Championships
    UNION ALL 
    SELECT US_open AS id FROM Championships
    UNION ALL 
    SELECT Au_open AS id FROM Championships 
   )
   
SELECT player_id,player_name ,COUNT(*) as grand_slams_count  FROM CTE
INNER JOIN Players
ON CTE.id = Players.player_id
GROUP BY player_id 
