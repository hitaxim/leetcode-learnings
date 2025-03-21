SELECT user_id, COUNT(*) as purchase_count
FROM Purchases
WHERE MONTH(purchase_date) = 8
GROUP BY user_id
HAVING COUNT(*) > 10
ORDER BY COUNT(*) DESC;
