# Write your MySQL query statement below
WITH PTS as (SELECT *,
CASE 
    WHEN host_goals > guest_goals then 3
    WHEN host_goals = guest_goals then 1
    ELSE 0
    END as host_PTS,
    
CASE 
    WHEN host_goals > guest_goals then 0
    WHEN host_goals = guest_goals then 1
    ELSE 3
    END as guest_PTS
FROM Matches
             ),
             
HOST as (
    SELECT team_name,team_id, coalesce(sum(host_PTS),0) as host_pts
    FROM Teams
    LEFT JOIN PTS
    ON Teams.team_id = PTS.host_team
    GROUP BY team_id
),

GUEST as (
    SELECT team_name,team_id, coalesce(sum(guest_PTS),0) as guest_pts
    FROM Teams
    LEFT JOIN PTS
    ON Teams.team_id = PTS.guest_team
    GROUP BY team_id
)

SELECT GUEST.team_id,GUEST.team_name,(host_pts+guest_pts) as num_points
FROM HOST
INNER JOIN GUEST
ON HOST.team_id = GUEST.team_id
ORDER BY num_points desc, GUEST.team_id asc
