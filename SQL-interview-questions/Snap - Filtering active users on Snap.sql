SELECT user_id 
FROM user_activity 
WHERE last_active_date >= '2021-08-01' 
AND friend_count > 5 
AND message_count >= 20;
