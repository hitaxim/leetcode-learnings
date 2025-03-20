SELECT C.customer_id, 
       C.first_name, 
       C.last_name, 
       C.app, 
       MAX(P.date) AS latest_purchase_date
FROM Customers C
JOIN Purchases P
ON C.customer_id = P.customer_id
GROUP BY C.customer_id, C.first_name, C.last_name, C.app;
