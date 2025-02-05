# Write your MySQL query statement below
SELECT DISTINCT product_id, 10 AS price FROM Products 
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM Products WHERE change_date <= '2019-08-16')
UNION
SELECT DISTINCT product_id, new_price AS price FROM Products 
WHERE (product_id, change_date) IN (SELECT product_id, MAX(change_date) AS DATE FROM Products  WHERE change_date <= '2019-08-16' GROUP BY product_id)
