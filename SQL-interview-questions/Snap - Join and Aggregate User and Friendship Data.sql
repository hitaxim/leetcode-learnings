SELECT u.user_id, u.user_name, COUNT(f.user_id1) AS num_accepted_requests
FROM users u
JOIN friendships f
ON u.user_id = f.user_id1
WHERE u.sign_up_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
AND f.status = 'Accepted'
GROUP BY u.user_id, u.user_name
HAVING num_accepted_requests >= 1;
