WITH private_events AS (
    SELECT user_id, event_id
    FROM event_rsvp
    WHERE attendance_status IN ('going', 'maybe')
      AND event_type = 'private'
),
user_pairs AS (
    SELECT 
        LEAST(e1.user_id, e2.user_id) AS user_a_id,
        GREATEST(e1.user_id, e2.user_id) AS user_b_id,
        COUNT(*) AS common_events
    FROM private_events e1
    JOIN private_events e2 
        ON e1.event_id = e2.event_id 
        AND e1.user_id < e2.user_id
    GROUP BY user_a_id, user_b_id
    HAVING COUNT(*) >= 2
)
SELECT up.user_a_id, up.user_b_id
FROM user_pairs up
JOIN friendship_status fs
    ON up.user_a_id = fs.user_a_id 
    AND up.user_b_id = fs.user_b_id
WHERE fs.status = 'not_friends';
