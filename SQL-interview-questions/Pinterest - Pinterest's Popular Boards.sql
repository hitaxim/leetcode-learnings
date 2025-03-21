SELECT
 u.username,
 b.board_id,
 b.followers_count
FROM
 Boards b
INNER JOIN Users u ON b.user_id = u.user_id
WHERE
 b.category = 'Home Decor'
ORDER BY 
 b.followers_count DESC
LIMIT 3;
