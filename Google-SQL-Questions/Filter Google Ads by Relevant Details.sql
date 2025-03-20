SELECT *
FROM ads
WHERE status = 'active'
AND impressions > 500000
AND YEAR(last_updated) = 2024;
