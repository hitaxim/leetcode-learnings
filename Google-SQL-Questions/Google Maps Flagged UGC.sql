WITH OffTopicCounts AS (
    SELECT 
        p.place_category, 
        COUNT(*) AS off_topic_count
    FROM maps_ugc_review m
    JOIN place_info p ON m.place_id = p.place_id
    WHERE m.content_tag = 'Off-topic'
    GROUP BY p.place_category
)
SELECT place_category AS off_topic_places
FROM OffTopicCounts
WHERE off_topic_count = (SELECT MAX(off_topic_count) FROM OffTopicCounts)
ORDER BY place_category;
