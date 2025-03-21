SELECT 
c.product_id, 
sum(case when a.add_id is not null then 1 else 0 end) / count(c.click_id) as conversion_rate
FROM 
clicks c
LEFT JOIN bag_adds a ON a.product_id = c.product_id AND a.user_id = c.user_id
GROUP BY c.product_id
