SELECT 
    campaign_id,
    ad_group_id, 
    SUM(cost) / SUM(clicks) AS avg_CPC
FROM 
    ad_clicks
GROUP BY 
    campaign_id, 
    ad_group_id;
