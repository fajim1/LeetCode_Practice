# Write your MySQL query statement below



SELECT ad_id, ifnull(round(sum(action='Clicked')*100/(sum(action='Clicked')+sum(action='Viewed')),2),0) as ctr

FROM Ads
GROUP BY ad_id
ORDER BY ctr desc, ad_id asc