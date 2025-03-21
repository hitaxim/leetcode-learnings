SELECT user_id, COUNT(*) AS num_snaps
FROM snaps
WHERE snap_date >= DATEADD(week, -4, '2022-09-06')
GROUP BY user_id
HAVING COUNT(*) > 400;

SELECT user_id, COUNT(*) AS num_snaps
FROM snaps
WHERE snap_date >= '2022-09-06' - INTERVAL '4 weeks'
GROUP BY user_id
HAVING COUNT(*) > 400;

SELECT user_id, COUNT(*) AS num_snaps
FROM snaps
WHERE snap_date >= DATE_SUB('2022-09-06', INTERVAL 4 WEEK)
GROUP BY user_id
HAVING COUNT(*) > 400;
