# Write your MySQL query statement below

With Bought as (
    SELECT stock_name, sum(price) as bought
    FROM Stocks
    WHERE operation='Buy'
    GROUP BY stock_name
    ),
Sold as (
    SELECT stock_name, sum(price) as sold
    FROM Stocks
    WHERE operation='Sell'
    GROUP BY stock_name
    )
    
SELECT Bought.stock_name, Sold.sold-Bought.bought as capital_gain_loss 
FROM Bought
INNER JOIN Sold
ON Bought.stock_name = Sold.stock_name

