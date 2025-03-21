SELECT 
    U.user_id,
    COALESCE(AVG(S.shares), 0) as avg_shares_per_post
FROM 
    user_posts as U
    LEFT JOIN (
        SELECT 
            post_id, 
            COUNT(share_id) as shares
        FROM 
            post_shares
        GROUP BY 
            post_id
        ) as S on U.post_id = S.post_id
GROUP BY 
    U.user_id;
