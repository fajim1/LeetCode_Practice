# Write your MySQL query statement below
WITH apple as (
    SELECT * 
    FROM Sales
    WHERE fruit = 'apples'

),

orange as (
    SELECT * 
    FROM Sales
    WHERE fruit = 'oranges'

)

SELECT apple.sale_date, apple.sold_num-orange.sold_num as diff
FROM apple
INNER JOIN orange
ON apple.sale_date = orange.sale_date