# Write your MySQL query statement below
(SELECT DISTINCT u.name AS results
FROM Users u
JOIN MovieRating m 
ON u.user_id = m.user_id
GROUP BY u.user_id
ORDER BY COUNT(*) DESC, u.name ASC
LIMIT 1)

UNION ALL
(
SELECT DISTINCT m1.title AS results
FROM Movies m1
JOIN MovieRating m
ON m1.movie_id = m.movie_id
WHERE YEAR(created_at) = '2020' AND MONTH(created_at) = '02'
GROUP BY m1.movie_id
ORDER BY AVG(m.rating) DESC, m1.title ASC
LIMIT 1
);
