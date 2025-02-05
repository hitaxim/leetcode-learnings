# Write your MySQL query statement below
SELECT DISTINCT visited_on, SUM(amount) OVER CTE AS amount, 
ROUND((SUM(amount) OVER CTE)/7,2) AS average_amount
FROM Customer

WINDOW CTE AS (
    ORDER BY visited_on
    RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
)
    LIMIT 6, 999
