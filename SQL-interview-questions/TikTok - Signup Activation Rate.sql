SELECT 
  ROUND(COUNT(t.email_id)::DECIMAL 
  /COUNT(DISTINCT e.email_id),2) AS activation_rate
FROM emails e 
LEFT JOIN texts t 
ON e.email_id = t.email_id 
AND t.signup_action = 'Confirmed';

"""
SELECT ROUND(CAST(COUNT(t.email_id) AS DECIMAL)/COUNT(DISTINCT e.email_id),2) AS activation_rate
FROM emails e 
LEFT JOIN texts t
ON e.email_id = t.email_id
AND t.signup_action = 'Confirmed';

  """
