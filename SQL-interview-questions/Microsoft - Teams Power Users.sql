SELECT sender_id, 
COUNT(message_id) AS message_count
FROM messages
WHERE EXTRACT(year FROM sent_date) = 2022 AND EXTRACT(month FROM sent_date) = 8
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 2;
