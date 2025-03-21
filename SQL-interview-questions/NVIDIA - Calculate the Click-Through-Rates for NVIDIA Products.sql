
SELECT v.product_id, 
       (CAST(COUNT(c.click_id) AS FLOAT) / COUNT(v.view_id)) * 100 AS click_through_rate
FROM product_views v
LEFT JOIN product_clicks c ON v.product_id = c.product_id AND v.user_id = c.user_id
WHERE v.view_date >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
AND v.view_date < DATE_TRUNC('month', CURRENT_DATE)
GROUP BY v.product_id
