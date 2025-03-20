SELECT
    up.user_id,
    COUNT(DISTINCT up.post_id) AS no_of_posts,
    AVG(pi.comments + pi.reactions) AS avg_interaction_per_post
FROM
    user_post up
JOIN
    post_interactions pi on up.post_id = pi.post_id
GROUP BY
    up.user_id
HAVING
    COUNT(DISTINCT up.post_id) >= 2 AND AVG(pi.comments + pi.reactions) >= 150
