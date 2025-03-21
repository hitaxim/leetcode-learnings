SELECT c.camp_name, 
        CAST(count(ac.click_id) AS FLOAT)/count(ai.impression_id) as CTR
FROM campaigns c 
LEFT JOIN ad_impressions ai on c.camp_id = ai.camp_id
LEFT JOIN ad_clicks ac on ai.impression_id = ac.click_id AND c.camp_id = ac.camp_id
GROUP BY c.camp_name;
