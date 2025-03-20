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



/*
WITH reviews AS (
    SELECT 
        place.place_category,
        COUNT(ugc.content_id) AS content_count
    FROM place_info place
    JOIN maps_ugc_review ugc
        ON place.place_id = ugc.place_id
    WHERE ugc.content_tag = 'Off-topic'
    GROUP BY place.place_category
)
SELECT 
    place_category,
    content_count,
    RANK() OVER (ORDER BY content_count DESC) AS top_place
FROM reviews;

*/
