SELECT c.customer_name,
       c.customer_email,
       SUM(p.product_price) as total_spent
FROM Customers c
JOIN Purchases p
ON c.customer_id = p.customer_id
WHERE p.product_id = 50001
GROUP BY c.customer_id
ORDER BY total_spent DESC
