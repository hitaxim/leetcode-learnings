SELECT DATE_PART('month', sale_date) AS month,
       product_id, 
       SUM(quantity) as total_quantity
FROM sales
WHERE DATE_PART('year', sale_date) = 2021
GROUP BY DATE_PART('month', sale_date), product_id
ORDER BY month, product_id;
