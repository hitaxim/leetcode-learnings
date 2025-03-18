WITH searches_expanded AS (
  SELECT searches
  FROM search_frequency
  GROUP BY 
    searches, 
    GENERATE_SERIES(1, num_users))

SELECT 
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (
    ORDER BY searches)::DECIMAL, 1) AS  median
FROM searches_expanded;


--- SOLUTION 2 -----
WITH cumulative_users AS (
    SELECT 
        searches, 
        num_users, 
        SUM(num_users) OVER (ORDER BY searches) AS running_total,
        SUM(num_users) OVER () AS total_users
    FROM search_frequency
)
SELECT ROUND(
    CASE 
        WHEN total_users % 2 = 1 THEN 
            (SELECT searches FROM cumulative_users 
             WHERE running_total >= (total_users + 1) / 2 
             ORDER BY running_total 
             LIMIT 1)
        ELSE 
            (SELECT AVG(searches * 1.0) FROM cumulative_users 
             WHERE running_total BETWEEN total_users / 2 AND (total_users / 2 + 1))
    END, 1) AS median
FROM cumulative_users
LIMIT 1;
