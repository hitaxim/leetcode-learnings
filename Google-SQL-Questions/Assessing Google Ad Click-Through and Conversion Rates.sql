SELECT 
  a.ad_id,
  COUNT(DISTINCT a.user_id) AS total_clicks,
  COUNT(DISTINCT c.user_id) AS total_conversions,
  COUNT(DISTINCT c.user_id)*1.0 / COUNT(DISTINCT a.user_id) * 100.0 AS conversion_rate
FROM 
  ad_clicks a
LEFT JOIN 
  cart_addition c
ON 
  a.ad_id = c.ad_id AND a.user_id = c.user_id
GROUP BY 
  a.ad_id;
