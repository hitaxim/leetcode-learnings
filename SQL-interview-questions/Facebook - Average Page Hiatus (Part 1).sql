SELECT 
	user_id, 
    MAX(post_date::DATE) - MIN(post_date::DATE) AS days_between
FROM posts
WHERE DATE_PART('year', post_date::DATE) = 2021 
GROUP BY user_id
HAVING COUNT(post_id)>1;

/*
SELECT user_id, 
MAX(CAST(post_date) AS DATE) - MIN(CAST(post_date) AS DATE) AS days_between
FROM posts
WHERE EXTRACT(year FROM post_date) = 2021
GROUP BY user_id
HAVING COUNT(post_id) > 1;
*/
