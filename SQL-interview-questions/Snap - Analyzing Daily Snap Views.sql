SELECT 
  snap_id,
  date,
  SUM(views) OVER (PARTITION BY snap_id ORDER BY date) as total_views_to_date,
  SUM(views) OVER (PARTITION BY snap_id ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as weekly_views
FROM
  daily_snap_analytics
ORDER BY
  snap_id,
  date;
