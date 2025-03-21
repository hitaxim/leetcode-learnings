WITH Click_Rates AS (
    SELECT product_category, COUNT(DISTINCT user_id) AS unique_clicks
    FROM clicks
    WHERE DATE(click_date) BETWEEN '2022-06-01' AND '2022-06-30'
    GROUP BY product_category),

Conversion_Rates AS (
    SELECT c.product_category, COUNT(DISTINCT v.user_id) AS unique_conversions
    FROM conversions v
    JOIN clicks c 
    ON c.product_id = v.product_id AND c.user_id = v.user_id  
    WHERE DATE(conversion_date) BETWEEN '2022-06-01' AND '2022-06-30'
    GROUP BY c.product_category)

SELECT Click_Rates.product_category,
    unique_clicks,
    COALESCE(unique_conversions, 0) AS unique_conversions,
    (unique_clicks * 1.0 / (SELECT COUNT(DISTINCT user_id) FROM clicks WHERE DATE(click_date) BETWEEN '2022-06-01' AND '2022-06-30')) AS click_through_rate,
    (COALESCE(unique_conversions, 0) * 1.0 / unique_clicks) AS conversion_rate
FROM Click_Rates
LEFT JOIN Conversion_Rates ON Click_Rates.product_category = Conversion_Rates.product_category
