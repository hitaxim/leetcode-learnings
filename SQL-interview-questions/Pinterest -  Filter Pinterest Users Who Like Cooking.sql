SELECT u.user_id, u.username
FROM users AS u 
JOIN (
  SELECT p.user_id
  FROM pins AS p
  WHERE p.category = 'Cooking'
  AND p.pinned_date > DATEADD(day, -30, GETDATE()) 
  GROUP BY p.user_id
  HAVING COUNT(p.pin_id) >= 5
) AS cooking_users ON u.user_id = cooking_users.user_id
WHERE NOT EXISTS (
  SELECT 1
  FROM pins AS p2
  WHERE p2.user_id = u.user_id
  AND p2.category = 'Gardening'
  AND p2.pinned_date > DATEADD(day, -30, GETDATE())
);
