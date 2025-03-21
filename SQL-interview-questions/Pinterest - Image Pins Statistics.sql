 SELECT
    EXTRACT(MONTH FROM pin_date) as month,
    user_id,
    COUNT(*) OVER(PARTITION BY user_id, EXTRACT(MONTH FROM pin_date)) as avg_monthly_pin,
    COUNT(*) OVER(PARTITION BY user_id, EXTRACT(MONTH FROM pin_date)) -
    LAG(COUNT(*)) OVER(PARTITION BY user_id order by EXTRACT(MONTH FROM pin_date)) as pin_change
FROM 
    pins
