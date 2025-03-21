SELECT MONTH(s.date_of_sale) as 'Month', p.product_name, AVG(s.quantity_sold) as 'Average_Sold'
FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE YEAR(s.date_of_sale) = 2021
GROUP BY Month, p.product_name
