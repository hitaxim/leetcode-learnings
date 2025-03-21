SELECT 
  sessions_1.session_id, 
  COUNT(sessions_2.session_id) AS concurrent_sessions 
FROM sessions AS sessions_1 
INNER JOIN sessions AS sessions_2 
  ON sessions_1.session_id != sessions_2.session_id
    AND (sessions_2.start_time BETWEEN sessions_1.start_time AND sessions_1.end_time
    OR sessions_1.start_time BETWEEN sessions_2.start_time AND sessions_2.end_time)
GROUP BY sessions_1.session_id
ORDER BY concurrent_sessions DESC;
