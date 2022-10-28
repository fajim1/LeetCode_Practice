# Write your MySQL query statement below
SELECT * , 
CASE 
    WHEN x+y > z and x+z>y and y+z > x then "Yes"
    ELSE "No"
    End as triangle
FROM Triangle