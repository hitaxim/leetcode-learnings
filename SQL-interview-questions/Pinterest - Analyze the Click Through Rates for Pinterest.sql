SELECT 
    a.ad_id, 
    (COUNT(c.click_id)/ COUNT(v.view_id))*100 as CTR
FROM 
    ad_clicks c
JOIN 
    ad_views v ON c.user_id = v.user_id AND c.ad_id = v.ad_id 
JOIN 
    ads a ON a.ad_id = c.ad_id
WHERE 
    EXTRACT(MONTH FROM click_date) = 7 AND EXTRACT(YEAR FROM click_date) = 2024
GROUP BY 
    a.ad_id
