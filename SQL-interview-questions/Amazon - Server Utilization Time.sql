WITH running_time 
AS (
  SELECT
    server_id,
    session_status,
    status_time AS start_time,
    LEAD(status_time) OVER (
      PARTITION BY server_id
      ORDER BY status_time) AS stop_time
  FROM server_utilization
)

SELECT
  DATE_PART('days', JUSTIFY_HOURS(SUM(stop_time - start_time))) AS total_uptime_days
FROM running_time
WHERE session_status = 'start'
  AND stop_time IS NOT NULL;

"""
  WITH server_sessions AS (
    SELECT 
        server_id, 
        status_time AS start_time,
        LEAD(status_time) OVER (PARTITION BY server_id ORDER BY status_time) AS stop_time
    FROM server_utilization
    WHERE session_status = 'start'
)
SELECT 
    FLOOR(SUM(EXTRACT(EPOCH FROM (stop_time - start_time))) / 86400) AS total_uptime_days
FROM server_sessions
WHERE stop_time IS NOT NULL;

"""
